import urllib.request
import random

url = "http://www.baidu.com"

ua_headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:57.0) Gecko/20100101 Firefox/57.0'
}
# 设置一个请求体
req = urllib.request.Request(url, headers=ua_headers)
# 发起请求
response = urllib.request.urlopen(req)
print(response.read())

agentStr = [
    "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.149 Safari/537.36",
    "Mozilla/5.0 (Linux; Android 5.0; SM-G900P Build/LRX21T) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.149 Mobile Safari/537.36",
    "Mozilla/5.0 (iPad; CPU OS 11_0 like Mac OS X) AppleWebKit/604.1.34 (KHTML, like Gecko) Version/11.0 Mobile/15A5341f Safari/604.1"]
# 第二种添加User-Agent的方式
req2 = urllib.request.Request(url)
req2.add_header("User-Agent", random.choice(agentStr))
response2 = urllib.request.urlopen(req2)
print(response2.read())
