from bs4 import BeautifulSoup

html_doc = """
<html><head><title>The Dormouse's story</title></head>
<body>
<p class="title"><b>The Dormouse's story</b></p>

<p class="story">Once upon a time there were three little sisters; and their names were
<a href="http://example.com/elsie" class="sister" id="link1">Elsie</a>,
<a href="http://example.com/lacie" class="sister" id="link2">Lacie</a> and
<a href="http://example.com/tillie" class="sister" id="link3">Tillie</a>;
and they lived at the bottom of a well.</p>

<p class="story">...</p>
"""
soup = BeautifulSoup(html_doc, features="html.parser")
# 格式化
# print(soup.prettify())
# 获取标签
print(soup.title)
# 获取标签的属性
print(soup.a)
print(soup.a.attrs['href'])
# 获取标签的子标签
print(list(soup.p.children))
print(list(soup.p.children)[0].text)
# 取出所有的a标签
print(soup.find_all("a"))
# 根据id找标签
print(soup.find(id="link3"))
# 找出所有的文字内容
print(soup.get_text())

# 支持css选择器
print(soup.select(".sister"))
print(dir(soup))
