#!/usr/bin/env sh
# Hearth & Hollow server start script. Installs NeoForge on first run, then starts the server.
set -eu
cd "$(dirname "$0")"

INSTALLER="neoforge-@NEOFORGE@-installer.jar"

if [ ! -f run.sh ]; then
  echo "Installing NeoForge @NEOFORGE@ (first run only)..."
  java -jar "$INSTALLER" --installServer
fi

# NeoForge's run.sh reads JVM flags from user_jvm_args.txt. Give it a heap size once; edit it after that.
if ! grep -q '^-Xmx' user_jvm_args.txt 2>/dev/null; then
  # The installer's file has no trailing newline, so start on a fresh line.
  printf '\n%s\n%s\n' '-Xms4G' '-Xmx6G' >> user_jvm_args.txt
fi

# First-run defaults only; an existing server.properties is never touched.
# allow-flight matters: without it the server kicks players using jetpacks or paragliders.
if [ ! -f server.properties ]; then
  printf '%s\n' 'allow-flight=true' 'view-distance=8' 'simulation-distance=6' 'spawn-protection=0' 'motd=Hearth & Hollow' > server.properties
fi

if ! grep -q '^eula=true' eula.txt 2>/dev/null; then
  echo "You need to accept the Minecraft EULA (https://aka.ms/MinecraftEULA) first:"
  echo "  echo eula=true > eula.txt"
  exit 1
fi

exec sh ./run.sh nogui "$@"
