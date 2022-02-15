from aip import AipOcr
import random
import os
import requests
from urllib import parse

# http://www.chictr.org.cn/Tools/verifyimagepage.aspx

def get_file_content(filePath):
    with open(filePath, 'rb') as fp:
        return fp.read()


if __name__ == "__main__":
    # APP_ID = '22039561'  # 刚才获取的 ID，下同
    # API_KEY = 'zOGTfeDX9dVcfoQXNrvKIW2O'
    # SECRECT_KEY = '8bWLRSkR7o5GqDGzSRQdmozOMEuynmMt'
    # client = AipOcr(APP_ID, API_KEY, SECRECT_KEY)
    # rand = random.random()
    # url = "http://www.chictr.org.cn/Tools/verifyimagepage.aspx?textcolor=2&bgcolor=F4F4F4&ut=1&time=" + str(rand)


    # image_dir = os.path.join(os.curdir, "images")
    # # 设置文件和文件名
    # filename = "verifycode.png"
    # filepath = os.path.join(image_dir, filename)
    # # 发送请求保存图片
    # resp = requests.get(url)
    # with open(filepath, "wb") as f:
    #     for chunk in resp.iter_content(1024):
    #         f.write(chunk)
    #
    # image = get_file_content('images/verifycode.png')
    # """ 带参数调用通用文字识别（高精度版） """
    # general = client.basicGeneral(image)
    # words = general["words_result"][0]["words"]
    # words = words.replace(" ", "")
    # print("识别内容为2：", words)

    page = None
    params = parse.parse_qs(parse.urlparse("http://www.chictr.org.cn/searchproj.aspx?verifycode=da638").query)
    if "page" in params:
        page = params["page"][0]
    else:
        page = 1


