from multiprocessing import Process, Queue
from time import sleep


def download(q):
    images = ['girl.jpg', 'boy.jpg', 'man.jpg']
    for image in images:
        print("正在下载：", image)
        sleep(0.5)
        q.put(image)
    pass


def getfile(q):
    while True:
        try:
            file = q.get(timeout=2)
            print(file, "保存成功")
        except:
            print("全部保存完毕")
            break



if __name__ == '__main__':
    q = Queue(5)
    p1 = Process(target=download, args=(q,))
    p2 = Process(target=getfile, args=(q,))

    p1.start()

    p2.start()
    # p1.join()
    # p2.join()

    print("主进程结束")
