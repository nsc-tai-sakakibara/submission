Attribute VB_Name = "Module2"
Option Explicit
'編集後
Sub consistency2()

Dim i As Long
Dim lastRow As Long
Dim lastCol As Long
Dim threshold As Boolean

Dim countCircle As Long
Dim countXmark As Long

'客先タイムシートの時間変換*****
lastRow = Cells(Rows.Count, 3).End(xlUp).Row
lastCol = Cells(Columns.Count, 3).End(xlToLeft).Column
countCircle = 0
countXmark = 0
threshold = True

For i = 3 To lastRow

'エラーコード*****
'社員番号
If Len(Cells(i, 1)) <> 6 Or Len(Cells(i, 4)) <> 6 Then

    MsgBox i & "社員番号が不正です"
    Cells(i, 9).Interior.ColorIndex = i
    threshold = False
    
ElseIf Cells(i, 1) <> Cells(i, 4) Then

    MsgBox i & "社員番号が異なっています"
    Cells(i, 9).Interior.ColorIndex = i
    threshold = False

End If

'名前
If Cells(i, 2) = "" Or Cells(i, 5) = "" Then

    MsgBox i & "名前の入力をしてください"
    Cells(i, 9).Interior.ColorIndex = i
    threshold = False
    
ElseIf Cells(i, 2) <> Cells(i, 5) Then

    MsgBox i & "名前が異なっています"
    Cells(i, 9).Interior.ColorIndex = i
    threshold = False
    
End If

'時間
If Cells(i, 3) = "" Or Cells(i, 6) = "" Then

    MsgBox i & "勤務時間の入力をしてください"
    Cells(i, 9).Interior.ColorIndex = i
    threshold = False
    
End If

Next

If threshold = False Then
    End
End If

For i = 3 To lastRow

'書式設定
Cells(i, 7).NumberFormatLocal = "[h]:mm"

Cells(i, 7).Value = Cells(i, 3) / 24

'〇×*****
If Left(Cells(i, 6), Len(Cells(i, 7))) = Left(Cells(i, 7), Len(Cells(i, 7))) Then
    Cells(i, 8).Value = "〇"
    countCircle = countCircle + 1
Else
    Cells(i, 8).Value = "×"
    countXmark = countXmark + 1
End If

Next

'Cells(lastRow - 1, lastCol + 2).Value = "〇の数：" & countCircle
'Cells(lastRow, lastCol + 2).Value = "×の数：" & countXmark

Range("j17").Value = "〇の数：" & countCircle
Range("j18").Value = "×の数：" & countXmark

'Columns(lastCol).AutoFit

Columns("a:j").AutoFit

End Sub
