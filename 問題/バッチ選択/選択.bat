@echo off

set number=
set /P number="1�`7 �ԍ����́F"

goto :label%number%

:label1
	echo ���1
	question1.bat
	goto :end

:label2
	echo ���2
	question2.bat
	goto :end

:label3
	echo ���3
	question3.bat
	goto :end

:label4
	echo ���4
	question4.bat
	goto :end

:label5
	echo ���5
	question5.bat
	goto :end

:label6
	echo ���6
	question6.bat
	goto :end

:label7
	echo ���7
	question7.bat
	goto :end

:end

pause