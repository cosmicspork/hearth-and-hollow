#!/usr/bin/env bash
# Boot a built server pack until it finishes loading, then stop it. Fails on a crash or timeout.
# Accepts the EULA inside the throwaway pack directory, so run it only in CI or a scratch copy.
#
# usage: boot_test.sh SERVER_PACK_DIR [TIMEOUT_SECONDS]
set -euo pipefail
dir=$1
timeout=${2:-600}
cd "$dir"

echo "eula=true" > eula.txt
printf '%s\n' 'view-distance=6' 'simulation-distance=4' 'motd=Hearth & Hollow boot test' > server.properties
mkfifo console
sh ./start.sh < console > boot.log 2>&1 &
pid=$!
exec 3> console

start=$SECONDS
until grep -q 'Done (' boot.log; do
  if ! kill -0 "$pid" 2>/dev/null; then
    echo "server exited before finishing startup"; tail -n 80 boot.log; exit 1
  fi
  if (( SECONDS - start > timeout )); then
    echo "server did not finish startup within ${timeout}s"; tail -n 80 boot.log; kill "$pid"; exit 1
  fi
  sleep 5
done
echo "started in $((SECONDS - start))s"

echo stop >&3
# The JVM sometimes saves everything and then lingers; give it a minute, then kill it.
for _ in $(seq 60); do kill -0 "$pid" 2>/dev/null || break; sleep 1; done
kill "$pid" 2>/dev/null || true
pkill -f "neoforge/.*/unix_args.txt" 2>/dev/null || true
if ls crash-reports/*.txt >/dev/null 2>&1; then
  echo "crash report written"; cat crash-reports/*.txt; exit 1
fi
grep -E '/ERROR\]' boot.log | grep -vE 'DISTXFORM|rsinsertexportupgrade|VersionChecker' || true
