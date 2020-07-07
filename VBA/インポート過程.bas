Attribute VB_Name = "�C���|�[�g�ߒ�"
Option Explicit
'�C���|�[�g�@�r��
Sub import()

    Dim ws As Worksheet
    Set ws = ThisWorkbook.Worksheets(4)

    Dim rb As Workbook
    Set rb = Workbooks.Open("201005�q��^�C���V�[�g.csv")
    Dim rs As Worksheet
    Set rs = rb.Worksheets("201005�q��^�C���V�[�g")

'�S�̕\��
    Dim i As Long
    Dim lastRow As Long
    lastRow = rs.Cells(Rows.Count, 3).End(xlUp).Row

    For i = 2 To lastRow
        ws.Cells(i, 2).Value = rs.Cells(i, 6).Value
        ws.Cells(i, 3).Value = rs.Cells(i, 8).Value
        ws.Cells(i, 4).Value = rs.Cells(i, 9).Value
        ws.Cells(i, 5).Value = rs.Cells(i, 10).Value

    Next

'1�s�\��

    ws.Cells(2, 7).Value = rs.Cells(2, 6).Value

'F�@+�@HIJ���Z���ʁ@�\��

    ws.Cells(2, 9).Value = rs.Cells(2, 6).Value
    ws.Cells(2, 10).Value = rs.Cells(2, 8).Value + rs.Cells(2, 9).Value + rs.Cells(2, 10).Value

'���v�\��
    
    ws.Cells(2, 12).Value = rs.Cells(2, 6).Value + rs.Cells(2, 8).Value + rs.Cells(2, 9).Value + rs.Cells(2, 10).Value
    
    rb.Close False
    Set rs = Nothing
    Set rb = Nothing

End Sub

Sub import2()

    Dim ws As Worksheet
    Set ws = ThisWorkbook.Worksheets(6)
    Dim color As Worksheet
    Set color = ThisWorkbook.Worksheets(2)

    Range("A1:C1").Merge
    Range("A1").Value = "�q��^�C���V�[�g"
    Range("D1:F1").Merge
    Range("D1").Name = "Socia"
    Range("A2").Name = "�Ј��ԍ�"
    Range("B2").Value = "����"
    Range("C2").Value = "����(h.mm)"
    Range("D2").Value = "�Ј��ԍ�"
    Range("E2").Value = "����"
    Range("F2").Value = "����(hh:mm)"
    Range("G2").Value = "�ϊ���"
    Range("H2").Value = "�`�F�b�N"

    Dim rb1 As Workbook
    Set rb1 = Workbooks.Open("C:\Users\PCsen\Desktop\data2\6��3��\201005�q��^�C���V�[�g.csv")
    Dim rs1 As Worksheet
    Set rs1 = rb1.Worksheets("201005�q��^�C���V�[�g")

    Dim i As Long
    
    Dim lastTime As Long
    lastTime = rs1.Cells(Rows.Count, 3).End(xlUp).Row
    
    For i = 2 To lastTime
        '�^�C���V�[�g
        ws.Cells(i + 1, 1).Value = rs1.Cells(i, 2).Value
        ws.Cells(i + 1, 2).Value = rs1.Cells(i, 3).Value
        ws.Cells(i + 1, 3).Value = (rs1.Cells(i, 6).Value + rs1.Cells(i, 8).Value + rs1.Cells(i, 9).Value + rs1.Cells(i, 10).Value)
    
    Next
    
    rb1.Close
    
    Dim rb2 As Workbook
    Set rb2 = Workbooks.Open("C:\Users\PCsen\Desktop\data2\6��3��\202005Socia.csv")
    Dim rs2 As Worksheet
    Set rs2 = rb2.Worksheets("202005Socia")
                
    Dim lastSocia As Long
    lastSocia = rs2.Cells(Rows.Count, 3).End(xlUp).Row
    Dim result As Variant
       
    For i = 2 To lastSocia
        
        'Socia
        ws.Cells(i + 1, 4).Value = rs2.Cells(i, 1).Value
        ws.Cells(i + 1, 5).Value = rs2.Cells(i, 2).Value
        
        ws.Cells(i + 1, 6).Value = rs2.Cells(i, 7).Value - rs2.Cells(i, 8).Value - rs2.Cells(i, 9).Value - rs2.Cells(i, 10).Value
        ws.Cells(i + 1, 6).NumberFormatLocal = "[h]:mm"

    Next
    
    rb2.Close
    
'    Debug.Print "cells" + CStr(ws.Cells(148, 1))
'
'    result = WorksheetFunction.Match(ws.Cells(148, 1).Value, ws.Range(ws.Cells(3, 4), ws.Cells(220, 4)), 0)
'
'    Debug.Print result
'
'    End
    
    For i = lastTime + 1 To 3 Step -1
            
        On Error GoTo error
        result = WorksheetFunction.Match(ws.Cells(i, 1).Value, ws.Range(ws.Cells(1, 4), ws.Cells(lastSocia, 4)), 0)
        ws.Cells(i, 9).Value = result
            
        Call ws.Cells(i, 1).Cut(ws.Cells(result, 1))
            
    Next
    
error:
    On Error GoTo 0

    Set rs1 = Nothing
    Set rb1 = Nothing
    Set rs2 = Nothing
    Set rb2 = Nothing

End Sub

