import requests
from bs4 import BeautifulSoup

url = 'https://katzeimmondlicht.github.io/%E5%BC%B1%E6%99%BA%E6%93%8D%E4%BD%9C/tags/'  # 替换为目标网页的URL
response = requests.get(url)
html_content = response.text

soup = BeautifulSoup(html_content, 'html.parser')

file = open("C:\Users\meow\Documents\katzeimMondlicht.github.io\弱智操作\此时标签.txt", "w", encoding='utf-8')

for p in divmod:
    file.write(p.text)
    file.write("\n")  # 写入换行符，每个 <p> 标签的文本占一行

# 关闭文件
file.close()
