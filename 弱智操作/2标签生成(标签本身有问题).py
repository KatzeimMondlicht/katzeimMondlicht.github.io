import os

words = []

# 打开txt文件
with open("D:\\记忆\\peony\\弱智操作\\tagtag.txt", "r", encoding="utf-8") as file:
    # 逐行读取文件内容
    for line in file:
        # 去除换行符并添加到词语列表中
        word = line.strip()
        words.append(word)

template = """---
layout: tag
title: {word}
---"""

# 指定保存文件的文件夹路径
output_folder = "D:\\记忆\\peony\\tag"

# 创建文件夹（如果不存在）
os.makedirs(output_folder, exist_ok=True)

for word in words:
    content = template.format(word=word)

    # 生成文件的文件名
    file_name = f"{word}.md"

    # 拼接文件的完整路径
    file_path = os.path.join(output_folder, file_name)

    with open(file_path, "w", encoding="utf-8") as file:
        file.write(content)

print("文件生成完毕！")