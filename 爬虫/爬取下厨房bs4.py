from bs4 import BeautifulSoup
import requests
import os
from urllib.parse import urlparse

r = requests.get("http://www.xiachufang.com/")
soup = BeautifulSoup(r.text, features="html.parser")

img_list = []
for img in soup.select("img"):
    if img.has_attr('data-src'):
        img_list.append(img.attrs["data-src"])
    else:
        img_list.append(img.attrs["src"])
# 初始化下载文件的目录
image_dir = os.path.join(os.curdir, "images")
if not os.path.isdir(image_dir):
    os.mkdir(image_dir)

for img in img_list:
    print(img)
    o = urlparse(img)
    # 设置文件和文件名
    filename = o.path[1:].split("@")[0]
    filepath = os.path.join(image_dir, filename)
    # # 发送请求保存图片
    url = "%s://%s/%s" % (o.scheme, o.netloc, filename)
    resp = requests.get(url)
    with open(filepath, "wb") as f:
        for chunk in resp.iter_content(1024):
            f.write(chunk)

