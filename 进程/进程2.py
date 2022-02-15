import threading
from multiprocessing import Process
from time import sleep

# 进程不可以共享全局变量

n = 0

def run1():
    global n
    for i in range(1000000):
        n += 1


def run2():
    global n
    for i in range(1000000):
        n += 1


if __name__ == '__main__':

    p1 = Process(target=run1)
    p1.start()
    p2 = Process(target=run2)
    p2.start()

    p1.join()
    p2.join()

    print("n",  n)
