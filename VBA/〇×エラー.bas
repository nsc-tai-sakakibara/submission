Attribute VB_Name = "Module2"
Option Explicit
'�ҏW��
Sub consistency2()

Dim i As Long
Dim lastRow As Long
Dim lastCol As Long
Dim threshold As Boolean

Dim countCircle As Long
Dim countXmark As Long

'�q��^�C���V�[�g�̎��ԕϊ�*****
lastRow = Cells(Rows.Count, 3).End(xlUp).Row
lastCol = Cells(Columns.Count, 3).End(xlToLeft).Column
countCircle = 0
countXmark = 0
threshold = True

For i = 3 To lastRow

'�G���[�R�[�h*****
'�Ј��ԍ�
If Len(Cells(i, 1)) <> 6 Or Len(Cells(i, 4)) <> 6 Then

    MsgBox i & "�Ј��ԍ����s���ł�"
    Cells(i, 9).Interior.ColorIndex = i
    threshold = False
    
ElseIf Cells(i, 1) <> Cells(i, 4) Then

    MsgBox i & "�Ј��ԍ����قȂ��Ă��܂�"
    Cells(i, 9).Interior.ColorIndex = i
    threshold = False

End If

'���O
If Cells(i, 2) = "" Or Cells(i, 5) = "" Then

    MsgBox i & "���O�̓��͂����Ă�������"
    Cells(i, 9).Interior.ColorIndex = i
    threshold = False
    
ElseIf Cells(i, 2) <> Cells(i, 5) Then

    MsgBox i & "���O���قȂ��Ă��܂�"
    Cells(i, 9).Interior.ColorIndex = i
    threshold = False
    
End If

'����
If Cells(i, 3) = "" Or Cells(i, 6) = "" Then

    MsgBox i & "�Ζ����Ԃ̓��͂����Ă�������"
    Cells(i, 9).Interior.ColorIndex = i
    threshold = False
    
End If

Next

If threshold = False Then
    End
End If

For i = 3 To lastRow

'�����ݒ�
Cells(i, 7).NumberFormatLocal = "[h]:mm"

Cells(i, 7).Value = Cells(i, 3) / 24

'�Z�~*****
If Left(Cells(i, 6), Len(Cells(i, 7))) = Left(Cells(i, 7), Len(Cells(i, 7))) Then
    Cells(i, 8).Value = "�Z"
    countCircle = countCircle + 1
Else
    Cells(i, 8).Value = "�~"
    countXmark = countXmark + 1
End If

Next

'Cells(lastRow - 1, lastCol + 2).Value = "�Z�̐��F" & countCircle
'Cells(lastRow, lastCol + 2).Value = "�~�̐��F" & countXmark

Range("j17").Value = "�Z�̐��F" & countCircle
Range("j18").Value = "�~�̐��F" & countXmark

'Columns(lastCol).AutoFit

Columns("a:j").AutoFit

End Sub
