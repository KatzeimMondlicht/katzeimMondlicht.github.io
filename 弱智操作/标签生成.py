import os

tags = [
“周记”,
“流水账”,
“Feel_the_rain”,
“誊写”,
“日记”,
“笔记”,
“观后感”,
“电影”,
“A6活页本”,
“事项”,
“下雨”,
“思索”,
“实习”,
“照片”,
“更新”,
“收集”,
“读书笔记”,
“死亡”,
]
template="""---
layout: tag
title: {tag}
---"""

# 指定保存文件的文件夹路径
output_folder = "C:\\Users\\meow\\Documents\\katzeimMondlicht.github.io\\tag"

# 创建文件夹（如果不存在）
os.makedirs(output_folder, exist_ok=True)

for tag in tags:
    content = template.format(tag=tag)

    # 生成文件的文件名
    file_name = f"{tag}.md"

    # 拼接文件的完整路径
    file_path = os.path.join(output_folder, file_name)

    with open(file_path, "w", encoding="utf-8") as file:
        file.write(content)

print("文件生成完毕！")
