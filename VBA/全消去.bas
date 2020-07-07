Attribute VB_Name = "ëSè¡ãé"
Option Explicit
'ï“èWå„
Sub delete2()

Dim i As Long
Dim lastRow As Long
Dim lastCol As Long

lastRow = Cells(Rows.Count, 3).End(xlUp).Row
lastCol = Cells(Columns.Count, 3).End(xlToLeft).Column

For i = 3 To lastRow

    Cells(i, 6).Interior.color = RGB(157, 195, 230)
    Cells(i, 3).Interior.color = RGB(157, 195, 230)
    Cells(i, 1).Interior.ColorIndex = 0
    Cells(i, 2).Interior.ColorIndex = 0
    Cells(i, 4).Interior.ColorIndex = 0
    Cells(i, 5).Interior.ColorIndex = 0

    Cells(i, 10).Value = ""
    Cells(i, 8).Value = ""
    Cells(i, 7).Value = ""

Next

'Range("A3:B18", "D3:E18").Interior.ColorIndex = 0

'Cells(lastRow - 1, lastCol + 2).Value = ""
'Cells(lastRow, lastCol + 2).Value = ""
Range("j17").Value = ""
Range("j18").Value = ""

End Sub
Sub example()
    MsgBox CStr(Cells(3, 6).Interior.color)
    Cells(3, 7).Interior.ColorIndex = 37
    Cells(3, 8).Interior.color = RGB(157, 195, 230)
    Cells(4, 4).Interior.color = Cells(4, 6).Interior.color
End Sub


