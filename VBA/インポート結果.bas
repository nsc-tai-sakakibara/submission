Attribute VB_Name = "インポート結果"
Option Explicit
'インポート完成
Sub import3()

    Dim ws As Worksheet
    Set ws = ThisWorkbook.Worksheets(7)
    
    Dim rb1 As Workbook
    Set rb1 = Workbooks.Open("C:\Users\PCsen\Desktop\data2\6月3日\201005客先タイムシート.csv")
    Dim rs1 As Worksheet
    Set rs1 = rb1.Worksheets("201005客先タイムシート")
    Dim i As Long, j As Long
    j = 3
    Dim number
    Dim tmp As String
    
    Set number = CreateObject("Scripting.Dictionary")
    
    Dim lastTime As Long
    lastTime = rs1.Cells(Rows.Count, 3).End(xlUp).Row
    
    For i = 3 To lastTime + 1
        'タイムシート
        ws.Cells(i, 1).Value = rs1.Cells(i - 1, 2).Value
        ws.Cells(i, 2).Value = rs1.Cells(i - 1, 3).Value
        ws.Cells(i, 3).Value = (rs1.Cells(i - 1, 6).Value + rs1.Cells(i - 1, 8).Value + rs1.Cells(i - 1, 9).Value + rs1.Cells(i - 1, 10).Value)
        
        ws.Cells(i, 3).Font.color = vbWhite
        ws.Cells(i, 3).Font.Bold = True
        ws.Cells(i, 3).Interior.color = RGB(157, 195, 230)
    
        tmp = ws.Cells(i, 1).Value
        number.Add tmp, tmp
        
    Next
    
    rb1.Close
    
    Dim rb2 As Workbook
    Set rb2 = Workbooks.Open("C:\Users\PCsen\Desktop\data2\6月3日\202005Socia.csv")
    Dim rs2 As Worksheet
    Set rs2 = rb2.Worksheets("202005Socia")
                
    Dim lastSocia As Long
    lastSocia = rs2.Cells(Rows.Count, 3).End(xlUp).Row
    Dim result As Variant
       
    For i = 2 To lastSocia
        
        'Socia
        tmp = rs2.Cells(i, 1).Value
        If number.exists(tmp) Then
        
            ws.Cells(j, 4).Value = rs2.Cells(i, 1).Value
            ws.Cells(j, 5).Value = rs2.Cells(i, 2).Value
        
            ws.Cells(j, 6).Value = rs2.Cells(i, 7).Value - rs2.Cells(i, 8).Value - rs2.Cells(i, 9).Value - rs2.Cells(i, 10).Value
            ws.Cells(j, 6).NumberFormatLocal = "[h]:mm:ss"
            
            ws.Cells(j, 6).Font.color = vbWhite
            ws.Cells(j, 6).Font.Bold = True

            'ws.Cells(j, 6).Interior.ColorIndex = ws.Cells(1, 1).Interior.ColorIndex
            ws.Cells(j, 6).Interior.color = RGB(157, 195, 230)
            j = j + 1
            
        End If
        
    Next
    
    rb2.Close

End Sub
