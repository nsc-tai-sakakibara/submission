@echo off
setLocal EnableDelayedExpansion

set x=1

FOR %%i in (*.txt) DO (
    rename %%i �t�@�C��!x!.txt
    set /a x+=1
)

pause