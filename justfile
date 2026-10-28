# Hearth & Hollow: `just` lists the recipes.

set shell := ["bash", "-euo", "pipefail", "-c"]

export PATH := env("HOME") / "go/bin:" + env("PATH")

prism := env("PRISM_DIR", env("HOME") / ".var/app/org.prismlauncher.PrismLauncher/data/PrismLauncher")
prism_cmd := env("PRISM_CMD", "flatpak run org.prismlauncher.PrismLauncher")
# A separate instance for local builds, so an install from CurseForge is never synced over.
instance := env("HH_INSTANCE", "Hearth & Hollow (dev)")
cache := "run/cache"
version := "dev"

default:
    @just --list

# Rebuild index.toml after changing anything in the pack
refresh:
    packwiz refresh

# Build the client and server zips into dist/, as a release does
build: server-pack
    mkdir -p dist
    packwiz curseforge export -o "dist/Hearth-and-Hollow-{{version}}.zip"
    rm -f "dist/Hearth-and-Hollow-{{version}}-server.zip"
    cd build/server && zip -qr "../../dist/Hearth-and-Hollow-{{version}}-server.zip" .
    ls -lh dist

# Build the server pack into build/server
server-pack: refresh
    python3 scripts/server_pack.py . build/server --cache {{cache}}

# Update the local server in run/server to the working copy and start it
server: server-pack
    #!/usr/bin/env bash
    set -euo pipefail
    command -v java >/dev/null || export PATH="{{prism}}/java/java-runtime-delta/bin:$PATH"
    mkdir -p run/server
    # Mods match the pack exactly; config and kubejs files are copied over the server's own.
    rsync -a --delete build/server/mods/ run/server/mods/
    rsync -a --exclude /mods/ build/server/ run/server/
    # start.sh installs NeoForge only when run.sh is missing.
    neoforge=$(sed -n 's/^neoforge = "\(.*\)"/\1/p' pack.toml)
    [ -d "run/server/libraries/net/neoforged/neoforge/$neoforge" ] || rm -f run/server/run.sh run/server/run.bat
    cd run/server
    exec ./start.sh

# Build the server pack and boot it once in build/server, as CI does
boot: server-pack
    command -v java >/dev/null || export PATH="{{prism}}/java/java-runtime-delta/bin:$PATH"; \
    scripts/boot_test.sh build/server 900

# Update the Prism instance in place to the working copy
sync *args: refresh
    python3 scripts/sync_instance.py . "{{prism}}/instances/{{instance}}" --cache {{cache}} {{args}}

# Sync the Prism instance, then launch it
play: sync
    nohup {{prism_cmd}} --launch "{{instance}}" >/dev/null 2>&1 &

# Regenerate the quest book in config/ftbquests from scripts/questgen
quests:
    python3 scripts/questgen/gen.py

# Check the quest chapters: ids exist in the pack, layouts fit, text follows the rules
quest-check:
    python3 scripts/questgen/check.py

# Index the dev instance's items, tags, biomes and more for quest-check (run `just sync` first)
quest-index:
    python3 scripts/questgen/build_index.py "{{prism}}/instances/{{instance}}/minecraft/mods" \
        "{{prism}}/libraries/com/mojang/minecraft/1.21.1/minecraft-1.21.1-client.jar" scripts/questgen/index

# Write the whole quest book as Markdown to run/quests.md, for reading it through
quest-book:
    mkdir -p run
    python3 scripts/questgen/export_md.py run/quests.md

# Add a mod from CurseForge: just add <slug, url or --addon-id N --file-id N>
add *args:
    packwiz curseforge add -y {{args}}
    packwiz refresh

# Update every unpinned mod to its newest 1.21.1 file
update:
    packwiz update --all -y
    packwiz refresh

# Delete build output (keeps the download cache in run/)
clean:
    rm -rf build dist
