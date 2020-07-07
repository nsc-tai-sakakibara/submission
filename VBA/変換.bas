Attribute VB_Name = "変換"
Option Explicit
'編集後
Sub consistency2()

Dim i As Long
Dim lastRow As Long
Dim lastCol As Long
Dim threshold As Boolean

Dim number
Dim tmp As String
Dim countCircle As Long
Dim countXmark As Long

'客先タイムシートの時間変換*****
lastRow = Cells(Rows.Count, 3).End(xlUp).Row
lastCol = Cells(Columns.Count, 3).End(xlToLeft).Column
countCircle = 0
countXmark = 0
threshold = True

Set number = CreateObject("Scripting.Dictionary")

For i = 3 To lastRow

'エラーコード*****
'社員番号
tmp = Cells(i, 1).Value

If Not Len(Cells(i, 1)) <> 6 Or Len(Cells(i, 1)) <> 5 Then

    Cells(i, 1).Interior.ColorIndex = 3
    Cells(i, 10).Value = "社員番号が不正です"
    
    threshold = False
    
ElseIf Not Len(Cells(i, 4)) <> 6 Or Len(Cells(i, 4)) <> 5 Then

    Cells(i, 4).Interior.ColorIndex = 3
    Cells(i, 10).Value = "社員番号が不正です"
    
    threshold = False

ElseIf Cells(i, 1) <> Cells(i, 4) Then

    Cells(i, 1).Interior.ColorIndex = 6
    Cells(i, 4).Interior.ColorIndex = 6
    Cells(i, 10).Value = "社員番号が異なっています"
    
    threshold = False

ElseIf Not number.exists(tmp) Then
    
    number.Add tmp, tmp
    Else
    Cells(i, 10).Value = "他の方と社員番号が同じです"
    Cells(i, 1).Interior.ColorIndex = 46
    Cells(i, 4).Interior.ColorIndex = 46

End If

'名前
If Cells(i, 2) = "" Then

    Cells(i, 2).Interior.ColorIndex = 3
    Cells(i, 10).Value = "名前を記入してください"
    
    threshold = False
ElseIf Cells(i, 5) = "" Then

    Cells(i, 5).Interior.ColorIndex = 3
    Cells(i, 10).Value = "名前を記入してください"
    
    threshold = False
    
ElseIf Cells(i, 2) <> Cells(i, 5) Then

    Cells(i, 2).Interior.ColorIndex = 6
    Cells(i, 5).Interior.ColorIndex = 6
    Cells(i, 10).Value = "名前が異なっています"
    
    threshold = False
    
End If

'時間
If Cells(i, 3) = "" Then

    Cells(i, 3).Interior.ColorIndex = 3
    Cells(i, 10).Value = "勤務時間を記入してください"
    
    threshold = False
    
ElseIf Cells(i, 6) = "" Then

    Cells(i, 6).Interior.ColorIndex = 3
    Cells(i, 10).Value = "勤務時間を記入してください"
    
    threshold = False
    
End If

Next

If threshold = False Then
    
    Columns("a:j").AutoFit
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

Range("j3").Value = "〇の数：" & countCircle
Range("j4").Value = "×の数：" & countXmark

'Columns(lastCol).AutoFit

Columns("a:j").AutoFit

End Sub

