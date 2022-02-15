from lxml import etree

html_doc = """
<html> 
  <head> 
    <title>The Dormouse's story</title> 
  </head>  
  <body> 
    <p class="title">
      <b>The Dormouse's story</b>
    </p>  
    <p class="story">Once upon a time there were three little sisters; and their names were 
      <a href="http://example.com/elsie" class="sister" id="link1">Elsie</a>, 
      <a href="http://example.com/lacie" class="sister" id="link2">Lacie</a> and 
      <a href="http://example.com/tillie" class="sister" id="link3">Tillie</a>; and they lived at the bottom of a well.
    </p>  
    <p class="story">...</p>
    <bookstore>
        <book class="book temp">
            <title lang="eng">Harry Potter</title>
            <price>29.99</price>
        </book>
        <book>
            <title lang="eng">Learning XML</title>
            <price>39.95</price>
        </book>
        <book class="book">
            <title lang="eng">活着</title>
            <price>69.99</price>
        </book>
        <book>
            <title lang="eng">骆驼祥子</title>
            <price>19.95</price>
        </book>
        <book>
            <title lang="eng">围城</title>
            <price>67</price>
        </book>
        <book>
            <title lang="eng">莎士比亚</title>
            <price>98</price>
        </book>
    </bookstore>
  </body> 
</html>

"""
selector = etree.HTML(html_doc)
links = selector.xpath("//p[@class='story']/a/@href")
for link in links:
    print(link)
# //：从任意字节点选取
print(selector.xpath("//p"))
# /：从根结点选取
print(selector.xpath("/p"))
# 选择文本
print(selector.xpath("//p/text()"))
# 多级筛选title
print("多级筛选", selector.xpath("//body//p/text()"))
# 当前节点
body = selector.xpath("/html/body")
print("当前节点", body[0].xpath("./p/text()"))
# 上级节点
print("上级节点", body[0].xpath("../head/title/text()"))
# 根据属性取字段
print("根据属性取字段", body[0].xpath("./p[@class='title']/b/text()"))
# 取属性
bookstore = selector.xpath("//bookstore")
print("取属性", bookstore[0].xpath("./book/title/@lang"))
# 选取书店第一本书的标题(注意，这里好像没有下标0)
print("选取书店第一本书的标题", bookstore[0].xpath("./book[1]/title/text()"))
# 选取书店最后一本书的标题
print("选取书店最后一本书的标题", bookstore[0].xpath("./book[last()]/title/text()"))
# 选取书店倒数第二本书的标题
print("选取书店倒数第二本书的标题", bookstore[0].xpath("./book[last()-1]/title/text()"))
# 选取书店前两本书的标题
print("选取书店前两本书的标题", bookstore[0].xpath("./book[position()<4]/title/text()"))
# 选取价格大于三十的书本的title
print("选取价格大于三十的书本的title", bookstore[0].xpath("./book[price>30]/title/text()"))
# 选取class中包含book的属性(注意不是等于)
print("选取class中包含book的属性", bookstore[0].xpath("./book[contains(@class, 'book')]/title/text()"))
