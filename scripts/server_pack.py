"""Build the server pack: server-side mods, the pack's config and kubejs, and start scripts.

Mod jars are fetched from the CurseForge CDN by the file id in each .pw.toml and checked against its
sha1. NeoForge is not bundled: the start scripts run its installer on first launch, because the
installer downloads the vanilla server jar, which can't be redistributed.

usage: server_pack.py PACK_DIR OUT_DIR [--cache DIR]
"""
import argparse, hashlib, shutil, sys, tomllib, urllib.parse, urllib.request
from pathlib import Path

UA = {"User-Agent": "hearth-and-hollow-build/1"}
COPY_DIRS = ("config", "defaultconfigs", "kubejs")
TEMPLATES = Path(__file__).parent / "server"


def fetch(url: str) -> bytes:
    with urllib.request.urlopen(urllib.request.Request(url, headers=UA), timeout=120) as r:
        return r.read()


def jar(meta: dict, cache: Path | None) -> bytes:
    """The file a .pw.toml describes, from the cache or the CurseForge CDN, checked against its sha1."""
    want = meta["download"]["hash"]
    cached = cache / want if cache else None
    if cached and cached.exists():
        data = cached.read_bytes()
    else:
        fid = meta["update"]["curseforge"]["file-id"]
        name = urllib.parse.quote(meta["filename"])
        data = fetch(f"https://mediafilez.forgecdn.net/files/{fid // 1000}/{fid % 1000}/{name}")
    if hashlib.sha1(data).hexdigest() != want:
        raise ValueError("sha1 mismatch")
    if cached and not cached.exists():
        cached.write_bytes(data)
    return data


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("pack", type=Path)
    ap.add_argument("out", type=Path)
    ap.add_argument("--cache", type=Path, help="directory of previously downloaded jars, keyed by sha1")
    args = ap.parse_args()

    pack = tomllib.loads((args.pack / "pack.toml").read_text())
    neoforge = pack["versions"]["neoforge"]
    if args.out.exists():
        shutil.rmtree(args.out)
    (args.out / "mods").mkdir(parents=True)
    if args.cache:
        args.cache.mkdir(parents=True, exist_ok=True)

    bad, count = [], 0
    for t in sorted((args.pack / "mods").glob("*.pw.toml")):
        m = tomllib.loads(t.read_text())
        if m["side"] == "client":
            continue
        try:
            data = jar(m, args.cache)
        except Exception as e:
            bad.append(f"{m['filename']}: {e}")
            continue
        (args.out / "mods" / m["filename"]).write_bytes(data)
        count += 1

    for d in COPY_DIRS:
        if (args.pack / d).is_dir():
            shutil.copytree(args.pack / d, args.out / d)

    installer = f"neoforge-{neoforge}-installer.jar"
    (args.out / installer).write_bytes(fetch(
        f"https://maven.neoforged.net/releases/net/neoforged/neoforge/{neoforge}/{installer}"))
    for f in TEMPLATES.iterdir():
        text = f.read_text().replace("@NEOFORGE@", neoforge)
        (args.out / f.name).write_text(text)
        if f.suffix == ".sh":
            (args.out / f.name).chmod(0o755)

    print(f"{count} server mods, NeoForge {neoforge}")
    if bad:
        print("problems:", *bad, sep="\n  ", file=sys.stderr)
        return 1
    return 0


if __name__ == "__main__":
    sys.exit(main())
