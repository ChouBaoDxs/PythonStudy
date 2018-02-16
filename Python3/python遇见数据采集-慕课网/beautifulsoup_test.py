# -*- coding: UTF-8 -*-
import re

from bs4 import BeautifulSoup as bs  # 设置别名bs

html_doc = """
<html><head><title>The Dormouse's story</title></head>
<body>
<p class="title"><b>The Dormouse's story</b></p>

<p class="story">Once upon a time there were three little sisters; and their names were
<a href="http://exampleS.com/elsie" class="sister" id="link1">Elsie</a>,
<a href="http://example.com/lacie" class="sister" id="link2">Lacie</a> and
<a href="http://example.com/tillie" class="sister" id="link3">Tillie</a>;
and they lived at the bottom of a well.</p>

<p class="story">...</p>
"""

soup = bs(html_doc, "html.parser")

print(soup.prettify())

print(soup.title.string)  # 打印title标签的文本内容
# print(soup.title.get_text())    #打印title标签的文本内容   区别是string只能获取一个标签里的内容

print(soup.a)  # 打印第一个a标签

print(soup.find(id="link2"))  # 打印id为link2的所有内容
print(soup.find(id="link2").string)  # 打印id为link2的文本内容
print(soup.find(id="link2").get_text())  # 打印id为link2的文本内容

print(soup.findAll("a"))  # 打印所有a标签
for link in soup.findAll("a"):
    print(link.string)

print("************************************************")
print(soup.find("p", {"class": "story"}))  # 打印P标签里的内容

print("************************************************")
print(soup.find("p", {"class": "story"}).get_text())  # 打印P标签里的文本内容

print("************************************************")
print(soup.find(class_="story"))  # 打印P标签里的内容

print("从文档中找到所有<a>标签的href链接:")
for link in soup.find_all('a'):
    print(link.get('href'))

print("从文档中找到所有以b开头的标签")
for tag in soup.find_all(re.compile("^b")):
    print(tag.name)

data = soup.findAll("a", href=re.compile(r"^http://example.com/"))  # 这样就打印不出修改过的link1了
print(data)
