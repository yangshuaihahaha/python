import queue  # 不能用于多进程之间的通讯，可以用于多线程间的通讯
from multiprocessing import Queue  # 可以用于进程之间的数据共享

q = Queue(3)  # 创建一个队列对象,队列长度为3
q.put(1)
q.put(2)

q.put(3)
# q.put(4)  # 当队列已满,继续放值,,会阻塞程序
try:
    q.put_nowait(4)  # 等同于 q.put(4, False)
except:
    print("队列已经满了.")
print(q.full())

print(q.get())
print(q.get())
print(q.get())
# print(q.get())  # 当队列空了,继续取值,也会阻塞程序
try:
    q.get_nowait()  # 等同于q.get(block=False)
except:
    print("队列已经空了.")
