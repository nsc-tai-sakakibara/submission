@echo off

set number=
set /P number="1〜7 番号入力："

goto :label%number%

:label1
	echo 問題1
	question1.bat
	goto :end

:label2
	echo 問題2
	question2.bat
	goto :end

:label3
	echo 問題3
	question3.bat
	goto :end

:label4
	echo 問題4
	question4.bat
	goto :end

:label5
	echo 問題5
	question5.bat
	goto :end

:label6
	echo 問題6
	question6.bat
	goto :end

:label7
	echo 問題7
	question7.bat
	goto :end

:end

pause