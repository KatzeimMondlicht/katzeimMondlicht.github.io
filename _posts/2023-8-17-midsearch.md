---
layout: post
title:  Excel中MID函数SEARCH函数使用方法
category: "笔记"
---
## 基础：MID(text, start_num, num_chars)

    =MID("Hello, World!", 8, 5)
这个例子中，我们从字符串"Hello, World!"中提取长度为5的子字符串。 `start_num` 参数为8，表示从第8个字符开始，所以提取的子字符串为"World"，最后的结果是"World"。

## 获取@用户名：之间的用户名

    =MID(A2,SEARCH("@",A2)+1,SEARCH("：",A2)-SEARCH("@",A2)-1)

## 获取文本中的http链接

    =MID(A2,SEARCH("http",A2),LEN(A2)-SEARCH("http",A2)+1)

## 从文本中提取（）内字符

    =MID(C1, FIND("（", C1)+1, FIND("）", C1)-FIND("（", C1)-1)

注意全角半角