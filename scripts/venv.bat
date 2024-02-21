@echo off
setlocal enabledelayedexpansion

for /f "tokens=* usebackq" %%a in (`.env`) do (
    set "line=%%a"
    if not "!line:~0,1!"=="#" (
        for /f "tokens=1* delims==" %%b in ("!line!") do (
            setx %%b %%c
        )
    )
)

echo Environment variables have been set.
