from time import sleep
from multiprocessing import Process



m = 1 #进程中各自拥有自己的变量

def task1(s):
    global m
    while True:
        sleep(s)
        m += 1
        print("这是任务1。。。。。。m: ", m)


def task2(s):
    global m
    while True:
        sleep(s)
        m += 1
        print("这是任务2。。。。。。m: ", m)


if __name__ == "__main__":
    p1 = Process(target=task1, args=[1])
    p1.start()
    p2 = Process(target=task2, args=[2])
    p2.start()
    num = 0
    while True:
        num += 1
        sleep(0.2)
        if num == 100:
            p1.terminate()
            p2.terminate()
            break
