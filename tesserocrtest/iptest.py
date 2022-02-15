import requests

def get_proxy():
    return requests.get("http://127.0.0.1:5010/get/").json()

def delete_proxy(proxy):
    requests.get("http://127.0.0.1:5010/delete/?proxy={}".format(proxy))

available_proxy = None
retry_count = 100
while retry_count > 0:
    proxy = get_proxy().get("proxy")
    html = requests.get('http://icanhazip.com', proxies={"http": "http://{}".format(proxy)})
    if html.status_code == 200:
        available_proxy = proxy
        break
    retry_count -= 1

if retry_count < 1:
    print("重试了100次也没有得到可用的IP ----------------------------------- ")
else:
    print("available_proxy ----------------------------------- " + available_proxy)