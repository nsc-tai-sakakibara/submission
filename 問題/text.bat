@echo off
setLocal EnableDelayedExpansion

set x
FOR %%i in (*.txt) DO(
    rename %%i ファイル!x!.txt
    set /a x+=1
)
pause