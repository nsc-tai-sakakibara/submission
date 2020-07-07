Attribute VB_Name = "Module1"
Option Explicit
'編集前
Sub consistency()

Dim i As Long
Dim last As Long

'客先タイムシートの時間変換*****
'値を確認して小数から分
last = Cells(Rows.Count, 3).End(xlUp).Row

For i = 3 To last

If Right(Cells(i, 3), 2) = "." Then

'　：〇〇　（：00）が変更していないのに追加されてしまう時がある  *60
Cells(i, 7).Value = Left(Cells(i, 3), 3) & ":30"
Else
Cells(i, 7).Value = Left(Cells(i, 3), 3) & ":00"
End If

'〇×
'=cells(i,7)だと×しか表示されない

If Left(Cells(i, 6), Len(Cells(i, 7))) = Left(Cells(i, 7), Len(Cells(i, 7))) Then
Range("H" & i).Value = "〇"
Else
Range("H" & i).Value = "×"
End If

Next

Columns("a:h").AutoFit

End Sub
