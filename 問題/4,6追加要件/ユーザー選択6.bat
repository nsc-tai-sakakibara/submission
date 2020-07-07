@echo off
setLocal EnableDelayedExpansion

set pass=
set /P pass="保存場所入力："

set format=
set /P format="フォーマット："

set file=
set /P file="ファイル名："

set x=1

FOR %%i in (%pass%.%format%) DO (
    rename %%i %file%!x!.%format%
    set /a x+=1
)

pause