Attribute VB_Name = "Module1"
Option Explicit
'�ҏW�O
Sub consistency()

Dim i As Long
Dim last As Long

'�q��^�C���V�[�g�̎��ԕϊ�*****
'�l���m�F���ď������番
last = Cells(Rows.Count, 3).End(xlUp).Row

For i = 3 To last

If Right(Cells(i, 3), 2) = "." Then

'�@�F�Z�Z�@�i�F00�j���ύX���Ă��Ȃ��̂ɒǉ�����Ă��܂���������  *60
Cells(i, 7).Value = Left(Cells(i, 3), 3) & ":30"
Else
Cells(i, 7).Value = Left(Cells(i, 3), 3) & ":00"
End If

'�Z�~
'=cells(i,7)���Ɓ~�����\������Ȃ�

If Left(Cells(i, 6), Len(Cells(i, 7))) = Left(Cells(i, 7), Len(Cells(i, 7))) Then
Range("H" & i).Value = "�Z"
Else
Range("H" & i).Value = "�~"
End If

Next

Columns("a:h").AutoFit

End Sub
