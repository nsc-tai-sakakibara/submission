@echo off

mkdir フォルダー

type null > ファイル1.txt
type null > ファイル2.txt
type null > ファイル3.txt
type null > ファイル4.txt
type null > ファイル5.txt

move ファイル1.txt .\フォルダー
move ファイル2.txt .\フォルダー
move ファイル3.txt .\フォルダー
move ファイル4.txt .\フォルダー
move ファイル5.txt .\フォルダー

pause