import urllib.request

urllib.request.urlretrieve("http://www.baidu.com", filename=r"/Users/yangshuai/PycharmProjects/demo/爬虫/fill2.html")

# urlretrieve执行的过程中，会产生一些缓存
# 清楚缓存
urllib.request.urlcleanup()