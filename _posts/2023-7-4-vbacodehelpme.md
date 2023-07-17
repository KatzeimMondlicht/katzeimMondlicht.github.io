---
layout: post
title:  "Excel从单元格提取特定颜色的文本"
category: "资料"
tags: [不能白写]
---
    Sub ExtractRedText()
        Dim rng As Range
        Dim cell As Range
        Dim text As String
        Dim i As Integer
        Dim redText As String
        
        Set rng = Range("H:H") '要操作的单元格范围，这里为H列
        
        For Each cell In rng
            text = cell.Text '获取单元格的文本
            
            For i = 1 To Len(text)
                If cell.Characters(i, 1).Font.Color = RGB(255, 0, 0) Then '判断字符的颜色是否为红色
                    redText = redText & Mid(text, i, 1) '将红色字符逐个添加到红色文本字符串
                End If
            Next i
            
            cell.Offset(0, 1).Value = redText '将红色文本放置到相邻单元格中
            
            redText = "" '重置红色文本字符串，准备处理下一个单元格
        Next cell
    End Sub


感恩chatgpt 没有你我会很为难（从每个包含黑色字体和红色字体的格子里提取红色字体）