import threading
from time import sleep

# 线程可以共享全局变量

money = 1000

def run1():
    global money
    for i in range(100):
        money -= 1


def run2():
    global money
    for i in range(100):
        money -= 1


if __name__ == '__main__':
    t1 = threading.Thread(target=run1, name="run1")
    t1.start()

    t2 = threading.Thread(target=run2, name="run2")
    t2.start()

    print("money",  money)
