@echo off

set /p url= "URLを入力："
set url= %url:https://=%
set url= %url:http://=%

ping %url%

pause