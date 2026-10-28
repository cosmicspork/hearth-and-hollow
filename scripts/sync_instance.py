"""Update a Prism Launcher instance to the working copy of the pack, in place.

Saves, options, keybinds and anything else the pack doesn't ship are left alone. What it does:

- mods/: made to match the pack exactly. Jars the pack doesn't list are deleted, so don't keep
  extra mods in a synced instance. A jar disabled in Prism (renamed to .disabled) stays disabled.
- shaderpacks/ and resourcepacks/: the pack's files are added or replaced; your own are kept.
- config/, kubejs/ and other overrides: copied from the files index.toml lists, so run
  `packwiz refresh` first. Files the pack stops shipping are deleted on the next sync, but only
  ones this script wrote (tracked in .hearth-sync.json in the instance).
- mmc-pack.json: the Minecraft and NeoForge versions are set to the pack's.

If the instance folder doesn't exist yet, it's created as a plain Prism instance named after the
folder. Prism downloads Minecraft and NeoForge on its first launch.

Default Options only applies config/defaultoptions on a first launch, so new default keybinds and
options don't reach an instance that already has options.txt.

usage: sync_instance.py PACK_DIR INSTANCE_DIR [--cache DIR] [--dry-run] [--force]
"""
import argparse, hashlib, json, os, sys, tomllib
from pathlib import Path

from server_pack import jar

META_DIRS = ("mods", "shaderpacks", "resourcepacks")
STATE = ".hearth-sync.json"


def sha1(path: Path) -> str:
    return hashlib.sha1(path.read_bytes()).hexdigest()


def running(instance: Path, game: Path) -> bool:
    """Whether a JVM is running from this instance: Prism starts it in the game folder."""
    needle, game = str(instance.resolve()).encode(), game.resolve()
    for proc in Path("/proc").glob("[0-9]*"):
        try:
            cmd = (proc / "cmdline").read_bytes()
            if b"java" in cmd and (needle in cmd or (proc / "cwd").resolve() == game):
                return True
        except OSError:
            continue
    return False


def create(instance: Path, pack_dir: Path):
    """A new, empty Prism instance; the sync below fills it and sets the versions."""
    pack = tomllib.loads((pack_dir / "pack.toml").read_text())
    (instance / "minecraft").mkdir(parents=True)
    (instance / "instance.cfg").write_text(
        f"[General]\nConfigVersion=1.3\nInstanceType=OneSix\niconKey=flame\nname={instance.name}\n")
    mmc = {"components": [
        {"uid": "net.minecraft", "version": pack["versions"]["minecraft"], "important": True},
        {"uid": "net.neoforged", "version": pack["versions"]["neoforge"]},
    ], "formatVersion": 1}
    (instance / "mmc-pack.json").write_text(json.dumps(mmc, indent=4) + "\n")
    print(f"created the Prism instance {instance.name}; restart Prism if it's open so it shows up")


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("pack", type=Path)
    ap.add_argument("instance", type=Path, help="the Prism instance folder, the one holding mmc-pack.json")
    ap.add_argument("--cache", type=Path, help="directory of previously downloaded jars, keyed by sha1")
    ap.add_argument("--dry-run", action="store_true", help="print the changes without making them")
    ap.add_argument("--force", action="store_true", help="sync even if the instance looks like it's running")
    args = ap.parse_args()

    if not args.instance.exists() and not args.dry_run:
        create(args.instance, args.pack)
    game = next((args.instance / d for d in ("minecraft", ".minecraft") if (args.instance / d).is_dir()), None)
    if game is None or not (args.instance / "mmc-pack.json").is_file():
        print(f"{args.instance} doesn't look like a Prism instance", file=sys.stderr)
        return 1
    if running(args.instance, game) and not args.force:
        print("the instance is running; quit the game first (or pass --force)", file=sys.stderr)
        return 1
    if args.cache:
        args.cache.mkdir(parents=True, exist_ok=True)

    dry = args.dry_run
    changes, bad = [], []

    def write(rel: str, data: bytes):
        dest = game / rel
        changes.append(f"{'replace' if dest.exists() else 'add':7} {rel}")
        if not dry:
            dest.parent.mkdir(parents=True, exist_ok=True)
            tmp = dest.with_name(dest.name + ".part")
            tmp.write_bytes(data)
            os.replace(tmp, dest)

    def delete(rel: str):
        changes.append(f"{'delete':7} {rel}")
        if not dry:
            (game / rel).unlink()

    # Mod jars, shaderpacks and resource packs, from their .pw.toml metadata.
    wanted: dict[str, dict] = {}
    for d in META_DIRS:
        for t in sorted((args.pack / d).glob("*.pw.toml")):
            m = tomllib.loads(t.read_text())
            if m["side"] != "server":
                wanted[f"{d}/{m['filename']}"] = m
    for rel, m in wanted.items():
        dest = game / rel
        if dest.with_name(dest.name + ".disabled").exists():
            continue
        if dest.exists() and sha1(dest) == m["download"]["hash"]:
            continue
        try:
            write(rel, jar(m, args.cache))
        except Exception as e:
            bad.append(f"{m['filename']}: {e}")

    if (game / "mods").is_dir():
        for f in sorted((game / "mods").glob("*.jar")):
            if f"mods/{f.name}" not in wanted:
                delete(f"mods/{f.name}")

    # Plain files (config, kubejs, ...): what packwiz exports as overrides.
    index = tomllib.loads((args.pack / "index.toml").read_text())
    shipped = sorted(f["file"] for f in index["files"] if not f.get("metafile"))
    for rel in shipped:
        data = (args.pack / rel).read_bytes()
        dest = game / rel
        if not (dest.exists() and dest.read_bytes() == data):
            write(rel, data)

    state_path = game / STATE
    previous = json.loads(state_path.read_text()) if state_path.exists() else {}
    current = shipped + [rel for rel in wanted if not rel.startswith("mods/")]
    for rel in sorted(set(previous.get("files", [])) - set(current)):
        if (game / rel).exists():
            delete(rel)

    # Prism re-resolves a component's libraries when its version changes.
    pack = tomllib.loads((args.pack / "pack.toml").read_text())
    versions = {"net.minecraft": pack["versions"]["minecraft"], "net.neoforged": pack["versions"]["neoforge"]}
    mmc_path = args.instance / "mmc-pack.json"
    mmc = json.loads(mmc_path.read_text())
    for c in mmc["components"]:
        want = versions.get(c["uid"])
        if want and c.get("version") != want:
            changes.append(f"{'set':7} {c['uid']} {c.get('version')} -> {want}")
            c["version"] = want
            c.pop("cachedVersion", None)
            c.pop("cachedRequires", None)

    if not dry:
        mmc_path.write_text(json.dumps(mmc, indent=4) + "\n")
        state_path.write_text(json.dumps({"files": current}, indent=1) + "\n")

    print("\n".join(changes) if changes else "already up to date")
    if dry and changes:
        print(f"{len(changes)} changes (dry run, nothing written)")
    if bad:
        print("problems:", *bad, sep="\n  ", file=sys.stderr)
        return 1
    return 0


if __name__ == "__main__":
    sys.exit(main())
