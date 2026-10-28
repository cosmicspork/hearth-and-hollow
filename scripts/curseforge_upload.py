"""Upload a release to CurseForge: the client pack zip, then the server pack as its additional file.

Needs CURSEFORGE_TOKEN (an API token from the CurseForge author settings) in the environment.

usage: curseforge_upload.py --project ID --version 0.2.0 --minecraft 1.21.1 \
           --pack PACK.zip [--server SERVER.zip] [--changelog FILE] [--release-type release]
"""
import argparse, json, os, sys, urllib.request, uuid
from pathlib import Path

API = "https://minecraft.curseforge.com/api"


def request(path, token, body=None, content_type=None):
    req = urllib.request.Request(f"{API}{path}", data=body, headers={"X-Api-Token": token, "User-Agent": "hearth-and-hollow-release/1"})
    if content_type:
        req.add_header("Content-Type", content_type)
    with urllib.request.urlopen(req, timeout=600) as r:
        return json.load(r)


def game_version_ids(token, minecraft):
    """CurseForge's ids for the Minecraft version, looked up rather than hardcoded."""
    types = {t["id"] for t in request("/game/version-types", token) if t["slug"].startswith("minecraft-")}
    ids = [v["id"] for v in request("/game/versions", token) if v["gameVersionTypeID"] in types and v["name"] == minecraft]
    if not ids:
        sys.exit(f"CurseForge has no game version named {minecraft}")
    return ids


def upload(project, token, file, metadata):
    boundary = uuid.uuid4().hex
    parts = [
        f'--{boundary}\r\nContent-Disposition: form-data; name="metadata"\r\n\r\n{json.dumps(metadata)}\r\n'.encode(),
        f'--{boundary}\r\nContent-Disposition: form-data; name="file"; filename="{file.name}"\r\n'
        f"Content-Type: application/zip\r\n\r\n".encode(),
        file.read_bytes(),
        f"\r\n--{boundary}--\r\n".encode(),
    ]
    result = request(f"/projects/{project}/upload-file", token, b"".join(parts), f"multipart/form-data; boundary={boundary}")
    return result["id"]


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--project", required=True)
    ap.add_argument("--version", required=True)
    ap.add_argument("--minecraft", required=True)
    ap.add_argument("--pack", type=Path, required=True)
    ap.add_argument("--server", type=Path)
    ap.add_argument("--changelog", type=Path)
    ap.add_argument("--release-type", default="release", choices=("release", "beta", "alpha"))
    args = ap.parse_args()

    token = os.environ["CURSEFORGE_TOKEN"]
    changelog = args.changelog.read_text() if args.changelog else f"Hearth & Hollow {args.version}"
    meta = {
        "changelog": changelog,
        "changelogType": "markdown",
        "displayName": f"Hearth & Hollow {args.version}",
        "gameVersions": game_version_ids(token, args.minecraft),
        "releaseType": args.release_type,
    }
    pack_id = upload(args.project, token, args.pack, meta)
    print(f"uploaded {args.pack.name} as file {pack_id}")

    if args.server:
        server_meta = {
            "changelog": changelog,
            "changelogType": "markdown",
            "displayName": f"Hearth & Hollow {args.version} Server",
            "parentFileID": pack_id,
            "releaseType": args.release_type,
        }
        server_id = upload(args.project, token, args.server, server_meta)
        print(f"uploaded {args.server.name} as file {server_id}")


if __name__ == "__main__":
    main()
