import threading
import time
from time import sleep

# 线程可以共享全局变量

lock = threading.Lock()

list1 = [0] * 10


def task1():
    # 获取线程锁，如果已经上锁，就等待锁释放
    lock.acquire()  # 阻塞
    for i in range(len(list1)):
        list1[i] = 1
        time.sleep(0.5)
    lock.release()


def task2():
    # 获取线程锁，如果已经上锁，就等待锁释放
    lock.acquire()  # 阻塞
    for i in range(len(list1)):
        print("------>", list1[i])
        time.sleep(0.5)
    lock.release()


if __name__ == '__main__':
    t1 = threading.Thread(target=task1)
    t2 = threading.Thread(target=task2)
    t1.start()
    t2.start()

