import requests
import threading
from bs4 import BeautifulSoup
from queue import Queue  # 可以用于进程之间的数据共享
from urllib.parse import urlparse
import os

link_queue = Queue()
threads_num = 10
threads = []


# 提取网页中图片的URL
def getUrl(url):
    r = requests.get(url)
    soup = BeautifulSoup(r.text, features="html.parser")

    img_list = []
    for img in soup.select("img"):
        if img.has_attr('data-src'):
            img_list.append(img.attrs["data-src"])
        else:
            img_list.append(img.attrs["src"])
    return img_list


def download():
    image_dir = os.path.join(os.curdir, "images")
    while True:
        # 阻塞直到从队列取得一条消息
        link = link_queue.get()
        if link is None:
            break
        o = urlparse(link)
        # 设置文件和文件名
        filename = o.path[1:].split("@")[0]
        filepath = os.path.join(image_dir, filename)
        # # 发送请求保存图片
        url = "%s://%s/%s" % (o.scheme, o.netloc, filename)
        resp = requests.get(url)
        with open(filepath, "wb") as f:
            for chunk in resp.iter_content(1024):
                f.write(chunk)
        link_queue.task_done()
        print("queue size:", link_queue.qsize())


if __name__ == '__main__':
    try:
        url = "http://www.xiachufang.com/"
        imglist = getUrl(url)

        # 将所有任务加入队列
        for i in range(len(imglist)):
            link_queue.put(imglist[i])

        # 启动线程，并将线程放入一个列表保存
        for i in range(threads_num):
            t = threading.Thread(target=download)
            t.start()
            threads.append(t)

        # 阻塞直到队列被清空
        link_queue.join()

        # 向线程发送N多个None，以通知线程退出
        for i in range(threads_num):
            link_queue.put(None)

        # 阻塞线程，直到线程退出
        for t in threads:
            t.join()
    except BaseException as e:
        print(e)

    print("Down")
