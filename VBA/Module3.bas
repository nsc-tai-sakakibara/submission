Attribute VB_Name = "Module3"
Option Explicit
'ï“èWëO
Sub delete()

Dim i As Long
Dim last As Long

last = Cells(Rows.Count, 1).End(xlUp).Row

For i = 3 To last

Cells(i, 8).delete shift:=xlToLeft
Cells(i, 7).delete shift:=xlToLeft

Next

End Sub
