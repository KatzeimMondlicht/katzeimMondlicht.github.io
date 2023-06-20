import requests
from bs4 import BeautifulSoup

url = 'https://katzeimmondlicht.github.io/%E5%BC%B1%E6%99%BA%E6%93%8D%E4%BD%9C/tags/'  # 替换为目标网页的URL
response = requests.get(url)
html_content = response.text
soup = BeautifulSoup(html_content, 'html.parser')

file_path = "D:\\记忆\\peony\\弱智操作\\tagtag.txt"

# 打开文件并写入内容
with open(file_path, "w", encoding='utf-8') as file:
    for p in soup.find_all("p"):
        file.write(p.text)
        file.write("\n")  # 写入换行符，每个 <p> 标签的文本占一行
# 唯一缺点是也爬到了标题下的阐述和结尾的话。
print("内容已保存到文件！")