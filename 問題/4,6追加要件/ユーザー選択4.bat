@echo off

set pass=
set /P pass="保存場所入力："

set file=
set /P file="ファイル名："

dir /b %pass% > %file%.txt

pause