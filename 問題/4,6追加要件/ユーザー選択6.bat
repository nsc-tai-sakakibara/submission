@echo off
setLocal EnableDelayedExpansion

set pass=
set /P pass="�ۑ��ꏊ���́F"

set format=
set /P format="�t�H�[�}�b�g�F"

set file=
set /P file="�t�@�C�����F"

set x=1

FOR %%i in (%pass%.%format%) DO (
    rename %%i %file%!x!.%format%
    set /a x+=1
)

pause