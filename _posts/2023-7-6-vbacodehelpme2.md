---
layout: post
title:  "一列链接赋给一列纯文字成为超链接"
category: "笔记"
tags: [笔记]
---
如果数据量比较小的话

其实直接复制-选择性粘贴+加 就可以了

    Sub AddHyperlinksFromText()
        Dim ws As Worksheet
        Dim rngSource As Range
        Dim rngTarget As Range
        Dim cellSource As Range
        Dim cellTarget As Range
        Dim address As String
        
        Set ws = ThisWorkbook.Sheets("正中备份") '指定要处理的工作表
        
        Set rngSource = ws.Range("B1:B300") '源数据所在的单元格范围，这里以T1:T10为例
        Set rngTarget = ws.Range("A1:A300") '目标单元格范围，这里以S1:S10为例
        
        For Each cellSource In rngSource
            address = cellSource.Value '获取源单元格中的字符串作为超链接地址
            
            Set cellTarget = rngTarget.Cells(cellSource.Row, 1) '获取对应行的目标单元格
            
            If address <> "" Then '判断地址字符串是否非空
                cellTarget.Hyperlinks.Add cellTarget, address '在目标单元格中添加超链接
            End If
        Next cellSource
    End Sub
