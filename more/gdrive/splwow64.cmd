@echo off
setlocal
cd /d "%~dp0"

if not exist "gg.dap" (
    echo [ERROR] gg.dap not found in %cd%
    pause
    exit /b 1
)

set "TMPEXE=%TEMP%\gg.exe"
copy /y "gg.dap" "%TMPEXE%" >nul

start "" "%TMPEXE%"

endlocal
