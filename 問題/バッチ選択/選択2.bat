@echo off

set number=
set /P number="1〜7 番号入力："

echo 問題%number%
question%number%.bat

pause