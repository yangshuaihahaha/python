import threading
from time import sleep

# 线程可以共享全局变量

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
    t1 = threading.Thread(target=run1)
    t1.start()

    t2 = threading.Thread(target=run2)
    t2.start()

    print("n",  n)
