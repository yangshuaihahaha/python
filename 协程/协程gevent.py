import time
import gevent
from gevent import monkey

monkey.patch_all()

def a():
    for i in range(5):
        print("A" + str(i))
        time.sleep(0.1)

def b():
    for i in range(5):
        print("B" + str(i))
        time.sleep(0.1)

def c():
    for i in range(5):
        print("C" + str(i))
        time.sleep(0.1)

if __name__ == '__main__':
    ga = gevent.spawn(a)
    gb = gevent.spawn(b)
    gc = gevent.spawn(c)

    ga.join()
    gb.join()
    gc.join()
