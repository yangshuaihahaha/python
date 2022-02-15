import urllib.request
import urllib.parse
import json
import time
import base64

with open('test.png', 'rb') as f:  # 以二进制读取本地图片
    data = f.read()
    encodestr = str(base64.b64encode(data), 'utf-8')
# 请求头
headers = {
    'Authorization': 'APPCODE e235e60e9a764592b42826748bd7c1ff',
    'Content-Type': 'application/json; charset=UTF-8'
}


def posturl(url, data={}):
    try:
        params = json.dumps(dict).encode(encoding='UTF8')
        req = urllib.request.Request(url, params, headers)
        r = urllib.request.urlopen(req)
        html = r.read()
        r.close();
        return html.decode("utf8")
    except urllib.error.HTTPError as e:
        print(e.code)
        print(e.read().decode("utf8"))
    time.sleep(1)


if __name__ == "__main__":
    url_request = "https://ocrapi-advanced.taobao.com/ocrservice/advanced"
    dict = {'img': encodestr}

    html = posturl(url_request, data=dict)
    print(html)
