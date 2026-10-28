# Running a Hearth & Hollow server

This guide covers hosting the pack for friends. If you use a Minecraft host with a CurseForge one-click installer, pick Hearth & Hollow there and skip to [Settings worth changing](#settings-worth-changing).

## What you need

- **Java 21.** On Linux use your package manager (for example `openjdk-21-jre-headless`); on Windows and macOS, [Adoptium Temurin 21](https://adoptium.net/temurin/releases/?version=21).
- **8 GB of RAM on the machine.** The server takes around 6 GB and the operating system needs the rest. A handful of players fits in that; give it more only if spark (see below) says it's short.
- **A fast CPU core and an SSD.** Minecraft servers run on mostly one thread, and world generation reads and writes a lot.

## Install

1. Download the **server pack** for your version. It's under *Additional Files* on the CurseForge file page, and attached to each [GitHub release](https://github.com/cosmicspork/hearth-and-hollow/releases).
2. Unzip it into an empty folder.
3. Read the [Minecraft EULA](https://aka.ms/MinecraftEULA). If you agree, create `eula.txt` in that folder containing:

   ```
   eula=true
   ```

4. Run `start.sh` (Linux and macOS) or `start.bat` (Windows).

The first run installs NeoForge, which downloads the Minecraft server from Mojang, and then starts the server. Later runs just start it. The first start takes a minute or two while mods load and the spawn area generates. It's ready when the console says `Done`.

Type `stop` in the console to shut down cleanly. Closing the window without stopping can lose the last few minutes of the world.

## Joining

Players need the **same pack version** as the server. The version shows on the title screen, and Better Compatibility Checker warns on join if it doesn't match.

- **Same network:** join with the server machine's local IP address.
- **Over the internet:** forward TCP port `25565` on your router to the server machine, then share your public IP. If you can't forward ports, a tunnel such as [playit.gg](https://playit.gg) works without it.

To make yourself an operator, run `op <your name>` in the server console.

## Settings worth changing

The start script writes a `server.properties` on the first run with values suited to this pack:

| Setting | Value | Why |
|---|---|---|
| `allow-flight` | `true` | Jetpacks and paragliders count as flying. With `false`, the server kicks players for using them. |
| `view-distance` | `8` | How far players see. Each step up costs memory and CPU for every player. |
| `simulation-distance` | `6` | How far crops grow and machines run around each player. |
| `spawn-protection` | `0` | Lets everyone build near spawn. |

After that the file is yours, and the script never touches it again. Other settings you may want:

- `white-list=true`, then `whitelist add <name>` for each friend, to keep strangers out.
- `difficulty=normal` or `hard`. The default is `easy`.
- `motd=...` for the line shown in the server list.

**Memory:** the heap is set in `user_jvm_args.txt` (`-Xms4G` and `-Xmx6G`). Change those two lines to give the server more or less. Leave a few GB for the operating system.

## Game rules

Game rules are saved with the world, not in `server.properties`, so set them once from the console after the first start. In game, an operator types the same with a `/` in front.

```
gamerule playersSleepingPercentage 0
```

That lets one player in bed skip the night for everyone. Use `50` to need half the players instead.

There's no need for `keepInventory`. When someone dies, their things go into a grave where they fell, and only they can open it.

## Claims and teams

FTB Chunks and FTB Teams are included. Players open the map (`M`) to claim chunks for their team and to force-load chunks so machines keep running while they're away. Inside a claim, explosions and mobs can't break blocks, and players outside the team can't either. The limits per player are in `config/ftbchunks-world.snbt`.

## Backups

Simple Backups is included and on by default. Out of the box it:

- makes a full backup every 2 hours, even if nobody is online
- keeps the newest 10, up to 25 GB
- writes them to the `simplebackups/` folder

Change any of that in `config/simplebackups-common.toml`. To restore, stop the server, move the broken `world/` folder aside, and unzip a backup in its place.

Copying `simplebackups/` to another disk now and then is still a good idea. A backup on the same drive won't survive that drive failing.

## Pregenerating the world

Generating new terrain is the most expensive thing the server does. Terralith and the structure mods make it heavier, and it shows as lag when several people explore at once. Generating the area around spawn ahead of time makes play much smoother.

The pack includes [Chunky](https://www.curseforge.com/minecraft/mc-mods/chunky-pregenerator-forge) for this. With the server running, type in the console:

```
chunky radius 2000
chunky start
```

That covers 4,000 by 4,000 blocks around spawn. Expect it to take a while, and run it when nobody is playing. `chunky pause` stops it and saves its progress, and `chunky continue` picks it up again, even after a restart. Chunky does nothing until you start it.

## Updating to a new version

1. Read the changelog. Removed mods delete their blocks and items from the world.
2. `stop` the server and back up the whole folder.
3. Delete `mods/`, `config/`, `kubejs/` and any `defaultconfigs/`, then unzip the new server pack over the folder.
4. Keep `world/`, `server.properties`, `user_jvm_args.txt`, `eula.txt`, the whitelist and ops files, and `simplebackups/`.
5. Start it.

If the new version uses a different NeoForge release, the start script won't reinstall it on its own. Delete `run.sh`, `run.bat` and `libraries/` before starting, and it will.

## When something goes wrong

- **Crashes:** look in `crash-reports/` and `logs/latest.log`.
- **Lag:** spark is included. Run `spark profiler start`, wait a minute while it lags, then `spark profiler stop`, and it prints a link to a report showing what's slow. `spark health` shows TPS and memory use.
- **Still stuck:** [open an issue](https://github.com/cosmicspork/hearth-and-hollow/issues/new) with the pack version, `logs/latest.log` and any crash report.
