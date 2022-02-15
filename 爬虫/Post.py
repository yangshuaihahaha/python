# 发送post请求分为表单类（x-www-form-urlencoded）和json（application/json）格式
#
# data参数支持字典格式和字符串格式，建议使用字典格式，在使用json.dumps()方法把data转换为合法的json格式字符串，或者将data参数赋值给post方法的json参数
#
# data以字符串格式传输需要注意的事项：
#
# 　　1、必须是json格式字符串，必须用双引号，k-v之家必须有逗号，布尔值必须是小写的true/false
#
# 　　2、不能有中文，直接传字符串不会自动编码

import urllib.request
import urllib.parse
import json

url = 'http://xxxx.com'
params = {
    "a": '1',
    "b": '2'
}

params = json.dumps(params)
headers = {'Accept-Charset': 'utf-8', 'Content-Type': 'application/json'}

req = urllib.request.Request(url=url, data=params, headers=headers, method='POST')
response = urllib.request.urlopen(req).read()
