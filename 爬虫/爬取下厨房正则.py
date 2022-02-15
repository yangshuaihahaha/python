import requests
import re

r = requests.get("https://www.baidu.com/")
print("r.text" + r.text)
# (?<=src=\") 匹配但是不包含
img_list = re.findall(r"(?<=src=\")http://i5\.chuimg\.com/\w+\.jpg", r.text)
print(img_list)
