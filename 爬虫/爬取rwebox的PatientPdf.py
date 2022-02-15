import requests
import threading
from queue import Queue
import os

patient_id_list = [118720, 118721, 118722, 118726, 118731, 118761, 118774, 118775, 118776, 118778]
patient_identifier_list = ['CHN14001', 'CHN25001', 'CHN25002', 'CHN03001', 'CHN03002', 'CHN08001', 'CHN03003',
                           'CHN02001', 'CHN02002', 'CHN15001']
link_queue = Queue()
threads_num = 10
threads = []

headers = {
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/85.0.4183.83 Safari/537.36',
    'Cookie': 'JSESSIONID=CE713662A44A537C5D5EFCA44CBD0B7E; cookieconsent_status=allow; _ga=GA1.2.730778457.1606706148; _gid=GA1.2.1484926063.1606877914; _gat_gtag_UA_121630108_1=1'
}


def download():
    pdf_dir = os.path.join(os.curdir, "pdf")
    while True:
        # 阻塞直到从队列取得一条消息
        obj = link_queue.get()
        if obj is None:
            break
        response = requests.get(obj["url"], headers=headers)
        # 设置文件和文件名
        filename = obj["name"] + ".pdf"
        filepath = os.path.join(pdf_dir, filename)
        with open(filepath, "wb") as f:
            for chunk in response.iter_content(1024):
                f.write(chunk)
        link_queue.task_done()
        print("queue size:", link_queue.qsize())


if __name__ == '__main__':
    try:
        # 将所有任务加入队列
        for index, id in enumerate(patient_id_list):
            url = "https://rwe.rwebox.com/rwe-web/patient/export/" + str(
                id) + ".page?pageSize=A4&orientation=Portrait&randomNum=2475056346.701366&displayId=false"
            obj = {"url": url, "name": patient_identifier_list[index]}
            link_queue.put(obj)

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
