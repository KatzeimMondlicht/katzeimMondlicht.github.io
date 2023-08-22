---
layout: post
title:  VBA代码每3行清除后2行/删除单元格前3位
category: "笔记"
tags: [笔记]
---
    Sub ClearRowsInSpecificSheet()
    Dim ws As Worksheet
    Dim lastRow As Long
    Dim rowNum As Long
    Dim rowCount As Long
    Dim i As Long
    
    ' 指定工作表名称
    Set ws = ThisWorkbook.Sheets("处理页")
    
    ' 设置起始行和每组行数
    rowNum = 1 ' 起始行号
    rowCount = 3 ' 每组行数
    
    ' 获取最后一行的行号
    lastRow = ws.Cells(Rows.Count, 1).End(xlUp).Row
    
    ' 循环处理每组行
    Do While rowNum <= lastRow
        ' 清除后两行数据
        For i = 1 To 2
            If rowNum + i <= lastRow Then
                ws.Rows(rowNum + i).ClearContents ' 清除内容
            End If
        Next i
        
        ' 移动到下一组行
        rowNum = rowNum + rowCount
    Loop
End Sub

如果想直接删除3行中的后两行：

    Sub ClearRowsInSpecificSheet()
    Dim ws As Worksheet
    Dim lastRow As Long
    Dim rowNum As Long
    Dim rowCount As Long
    Dim i As Long
    
    ' 指定工作表名称
    Set ws = ThisWorkbook.Sheets("处理页")
    
    ' 设置起始行和每组行数
    rowNum = 1 ' 起始行号
    rowCount = 3 ' 每组行数
    
    ' 获取最后一行的行号
    lastRow = ws.Cells(Rows.Count, 1).End(xlUp).Row
    
    ' 循环处理每组行
    Do While rowNum <= lastRow
        ' 清除后两行数据
        For i = 1 To 2
            If rowNum + i <= lastRow Then
                ws.Rows(rowNum + i).ClearContents ' 清除内容
            End If
        Next i
        
        ' 移动到下一组行
        rowNum = rowNum + rowCount
    Loop
End Sub

如果只想删除空行：

    Sub DeleteBlankRowsInSpecificSheet()
    Dim ws As Worksheet
    Dim lastRow As Long
    Dim i As Long
    
    ' 指定工作表名称
    Set ws = ThisWorkbook.Sheets("Sheet1")
    
    ' 获取最后一行的行号
    lastRow = ws.Cells(Rows.Count, 1).End(xlUp).Row
    
    ' 从最后一行往上遍历每一行
    For i = lastRow To 1 Step -1
        ' 检查当前行是否是空行
        If WorksheetFunction.CountA(ws.Rows(i)) = 0 Then
            ws.Rows(i).Delete ' 删除空行
        End If
    Next i
End Sub

删除单元格前3位

    Sub DeleteFirstThreeCharacters()
    Dim ws As Worksheet
    Dim lastRow As Long
    Dim rng As Range
    Dim cell As Range
    
    ' 设置工作表
    Set ws = ThisWorkbook.Sheets("Sheet1") ' 将 "Sheet1" 替换为你的工作表名称
    
    ' 找到最后一行
    lastRow = ws.Cells(ws.Rows.Count, "A").End(xlUp).Row
    
    ' 设置要处理的范围（这里假设你要处理的是 A 列）
    Set rng = ws.Range("A1:A" & lastRow)
    
    ' 循环处理每个单元格
    For Each cell In rng
        If Len(cell.Value) > 3 Then
            cell.Value = Mid(cell.Value, 4) ' 删除前3个字符
        End If
    Next cell
End Sub
