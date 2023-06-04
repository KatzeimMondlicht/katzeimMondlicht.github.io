import os

tags = [
    "音乐",
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
