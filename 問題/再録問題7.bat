@echo off

set /p url= "URL����́F"
set url= %url:https://=%
set url= %url:http://=%

ping %url%

pause