# ptthon 安装一定要add to path
import requests
from bs4 import BeautifulSoup

# 发起请求获取网页内容
url = 'https://katzeimmondlicht.github.io/%E5%BC%B1%E6%99%BA%E6%93%8D%E4%BD%9C/tags/'  # 替换为目标网页的URL
response = requests.get(url)
html_content = response.text

# 使用BeautifulSoup解析网页内容
soup = BeautifulSoup(html_content, 'html.parser')

# 找到网页正文的相关元素或标签
paragraphs = soup.find_all("p")
for p in paragraphs:
    print(p.text)

# 打开文件，指定文件名和打开模式（写入模式）
file = open("C:\Users\meow\Documents\katzeimMondlicht.github.io\弱智操作\此时标签.txt", "w", encoding='utf-8')

# 遍历 <p> 标签，将文本内容写入文件
for p in paragraphs:
    file.write(p.text)
    file.write("\n")  # 写入换行符，每个 <p> 标签的文本占一行

# 关闭文件
file.close()
