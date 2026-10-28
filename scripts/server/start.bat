@echo off
rem Hearth & Hollow server start script. Installs NeoForge on first run, then starts the server.
cd /d "%~dp0"

set INSTALLER=neoforge-@NEOFORGE@-installer.jar

if not exist run.bat (
  echo Installing NeoForge @NEOFORGE@ ^(first run only^)...
  java -jar "%INSTALLER%" --installServer || exit /b 1
)

rem NeoForge's run.bat reads JVM flags from user_jvm_args.txt. Give it a heap size once; edit it after that.
findstr /b /c:"-Xmx" user_jvm_args.txt >nul 2>&1 || (
  rem The installer's file has no trailing newline, so start on a fresh line.
  echo.>> user_jvm_args.txt
  echo -Xms4G>> user_jvm_args.txt
  echo -Xmx6G>> user_jvm_args.txt
)

rem First-run defaults only; an existing server.properties is never touched.
rem allow-flight matters: without it the server kicks players using jetpacks or paragliders.
if not exist server.properties (
  echo allow-flight=true> server.properties
  echo view-distance=8>> server.properties
  echo simulation-distance=6>> server.properties
  echo spawn-protection=0>> server.properties
  echo motd=Hearth ^& Hollow>> server.properties
)

findstr /b /c:"eula=true" eula.txt >nul 2>&1 || (
  echo You need to accept the Minecraft EULA ^(https://aka.ms/MinecraftEULA^) first:
  echo   echo eula=true ^> eula.txt
  pause
  exit /b 1
)

call run.bat nogui %*
