import urllib.request

for i in range(1, 100):
    try:
        response = urllib.request.urlopen(r"http://www.baidu.com", timeout=0.02)
    except:
        print("请求超时。失败")
