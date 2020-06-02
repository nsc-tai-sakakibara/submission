@echo off

set /p url= "URL‚ğ“ü—ÍF"
set url= %url:https://=%
set url= %url:http://=%

ping %url%

pause