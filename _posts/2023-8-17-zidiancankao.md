---
layout: post
title:  VBA代码以分类页做参考自动数据分类
category: "笔记"
tags: [笔记]
---
一些简单有参考的数据分类

把分类页的AB列数据做为词典

然后循环对照填写

（爆炸好用 感恩计算机）

    Sub Fill-FromReference()
        Dim wsMain As Worksheet
        Dim wsReference As Worksheet
        Dim mainValue As String
        Dim referenceRange As Range
        Dim foundCell As Range
        Dim lastRow As Long
        Dim i As Long
        
        ' 设置分类页工作表和主工作表
        Set wsMain = ThisWorkbook.Sheets("主工作表名")
        Set wsReference = ThisWorkbook.Sheets("分类页")
        
        ' 获取主工作表最后一行的行号
        lastRow = wsMain.Cells(wsMain.Rows.Count, "D").End(xlUp).Row
        
        ' 设置分类页的查找范围为 A 列
        Set referenceRange = wsReference.Range("A:A")
        
        ' 循环每一行
        For i = 1 To lastRow
            ' 获取主要列中的值
            mainValue = wsMain.Cells(i, "D").Value
            
            ' 在分类页中查找匹配的值
            Set foundCell = referenceRange.Find(What:=mainValue, LookIn:=xlValues, LookAt:=xlWhole)
            
            If Not foundCell Is Nothing Then
                ' 如果找到匹配的值，则填写
                wsMain.Cells(i, "G").Value = foundCell.Offset(0, 1).Value
            Else
                ' 如果未找到匹配的值，则填写空值
                wsMain.Cells(i, "G").Value = ""
            End If
        Next i
    End Sub