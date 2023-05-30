import requests
from bs4 import BeautifulSoup

# 发起请求获取网页内容
url = 'https://katzeimmondlicht.github.io/%E5%BC%B1%E6%99%BA%E6%93%8D%E4%BD%9C/tags/'  # 替换为目标网页的URL
response = requests.get(url)
html_content = response.text

# 使用BeautifulSoup解析网页内容
soup = BeautifulSoup(html_content, 'html.parser')

# 找到网页正文的相关元素或标签
# 找到目标标签
tag = soup.find('p')

# 提取标签中的文本内容
if tag:
    text = tag.get_text()
    print(text)
else:
    print("未找到目标标签")
