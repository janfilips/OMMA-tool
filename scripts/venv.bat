@echo off
setlocal enabledelayedexpansion

for /f "tokens=* delims=" %%a in (.env.local) do (
    set "line=%%a"
    if not "!line:~0,1!"=="#" (
        for /f "tokens=1* delims==" %%b in ("!line!") do (
            setx %%b %%c
            echo %%b=%%c
        )
    )
)

echo All environment variables have been set and displayed.
