---
layout: post
title:  "一列链接赋给一列纯文字成为超链接"
category: "笔记"
tags: [笔记]
---
如果你想将T列单元格中的字符串作为超链接赋予S列，可以使用以下VBA代码来实现：
    
    Sub AddHyperlinksFromText()
        Dim ws As Worksheet
        Dim rngSource As Range
        Dim rngTarget As Range
        Dim cellSource As Range
        Dim cellTarget As Range
        Dim address As String
        
        Set ws = ThisWorkbook.Sheets("Sheet1") '指定要处理的工作表
        
        Set rngSource = ws.Range("T1:T10") '源数据所在的单元格范围，这里以T1:T10为例
        Set rngTarget = ws.Range("S1:S10") '目标单元格范围，这里以S1:S10为例
        
        For Each cellSource In rngSource
            address = cellSource.Value '获取源单元格中的字符串作为超链接地址
            
            Set cellTarget = rngTarget.Cells(cellSource.Row, 1) '获取对应行的目标单元格
            
            If address <> "" Then '判断地址字符串是否非空
                cellTarget.Hyperlinks.Add cellTarget, address '在目标单元格中添加超链接
            End If
        Next cellSource
    End Sub
感恩chatgpt 唯一的问题是这个会复制串行 有空再研究叭先吃个饭