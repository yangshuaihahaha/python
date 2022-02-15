import threading
from time import sleep


def download(s):
    images = ['girl.jpg', 'boy.jpg', 'man.jpg']
    for image in images:
        print("正在下载：", image)
        sleep(s)
        print("下载成功：", image)


def listenMusic(s):
    musics = ['勇气', '出山', '骆驼', '练习', '波斯猫', '玫瑰花的葬礼']
    for music in musics:
        print("正在听：", music)
        sleep(s)
        print("听歌结束：", music)


if __name__ == '__main__':
    t1 = threading.Thread(target=download, args=(0.5,), name="aa")
    t1.start()

    t2 = threading.Thread(target=listenMusic, args=(0.5,), name="aa")
    t2.start()

    n = 1
    while True:
        n += 1
        sleep(2)
        print("主进程", n)
