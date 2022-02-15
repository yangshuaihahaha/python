import requests

# GET
r = requests.get("http://httpbin.org/get", params={"a": "1", "b": "2"})
print(r.status_code, r.reason)
print(r.text)
# POST
r2 = requests.post("http://www.httpbin.org/post", data={"a": "1", "b": "2"})
print(r2.text)
print(r2.json())
# headers
headers = {
    "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.149 Safari/537.36"
}
r3 = requests.get("http://www.httpbin.org/headers", headers=headers)
print(r3.headers)
# cooks
cookies = dict(userid="123456", token="xxxxxxxxx")
r4 = requests.get("http://www.httpbin.org/cookies", cookies=cookies)
print(r4.json())
# auth
r5 = requests.get("http://www.httpbin.org/basic-auth/123456/xxxxxx")
print("auth", r5.text)
# session
# 创建session
s = requests.Session()
# session对象保存服务器返回的set-cookies头信息
s.get("http://httpbin.org/cookies/set/userid/12345678")
s.get("http://httpbin.org/cookies/set/token/12345678")
# 下一次请求会自动将本地所有的请求头信息自动添加到请求头信息里面
r = s.get("http://httpbin.org/cookies")
print("检车session中的cookies", r.json())
# 在request中使用代理
print("不使用代理：", requests.get("http://httpbin.org/ip").json())
print("使用代理：", requests.get("http://httpbin.org/ip", proxies={"http": "http://iguye.com:41801"}).json())
# timeout
r = requests.get("http://httpbin.org/delay/2", timeout=2)
print(r.text)
