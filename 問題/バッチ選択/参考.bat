@echo off
REM ----- メニュー表示バッチ・ファイル
 
:TOP
 
echo *****************************************************************
echo * menu                                                          *
echo *                                                               *
echo *   1:メモ帳                                                    *
echo *   2:ペイント                                                  *
echo *   3:電卓                                                      *
echo *  99:終了                                                      *
echo *                                                               *
echo *****************************************************************
 
:MENUSTART
 
set USR_INPUT_STR=
set /P USR_INPUT_STR="番号を入力してください: "
 
if %USR_INPUT_STR%==1 (
  goto EXECUTE_NOTEPAD
) else if %USR_INPUT_STR%==2 (
  goto EXECUTE_PAINT
) else if %USR_INPUT_STR%==3 (
  goto EXECUTE_CALC
) else if %USR_INPUT_STR%==99 (
  goto EXITTRAP
) else (
  echo メニューにその番号はありません。
  echo.
  goto MENUSTART
)
 
REM メモ帳の起動
:EXECUTE_NOTEPAD
notepad
cls
goto TOP
 
REM ペイントの起動
:EXECUTE_PAINT
mspaint
cls
goto TOP
 
REM 電卓の起動
:EXECUTE_CALC
calc
cls
goto TOP
 
:EXITTRAP
echo.
echo 終了します。
pause