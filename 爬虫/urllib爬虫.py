import urllib.request

response = urllib.request.urlopen("http://www.baidu.com")

data = response.read()
data2 = response.readlines()

print(data2)
print(type(data2))
print(len(data2))


# response 的属性
# 信息
print(response.info())
# 状态码
print(response.getcode())
# 地址
print(response.geturl())
# 解码
url = r"https://list.tmall.com/search_product.htm?q=%E6%89%8B%E6%9C%BA&ali_trackid=2:mm_26632258_3504122_57418735:1585375960_103_1754341714&clk1=0f3b142598d66be8a3bcaacd6cc1ad73&upsid=0f3b142598d66be8a3bcaacd6cc1ad73"
newUrl = urllib.request.unquote(url)
print(newUrl)
# 编码
newUrl2 = urllib.request.quote(url)
print(newUrl2) 









# data2 = str(data, encoding="utf-8")
#
# with open("/Users/yangshuai/PycharmProjects/demo/爬虫/fill1.html", "wb") as f:
#     f.write(bytes(data, encoding="utf-8"))

# Python中的str与bytes之间的转换的三种方法
# bytes object
b = b"example"

# str object
s = "example"

# str to bytes
sb = bytes(s, encoding="utf8")

# bytes to str
bs = str(b, encoding="utf8")

# an alternative method
# str to bytes
sb2 = str.encode(s)

# bytes to str
bs2 = bytes.decode(b)
