import os
from multiprocessing import Pool
import time
from random import random


# 阻塞式
# 添加一个执行一个，如果一个任务不结束，另一个任务就进不来
def task(task_name):
    try:
        print("开始", task_name)
        start = time.time()
        time.sleep(random() * 3)
        end = time.time()
        print("完成任务{}，用时: {}, 进程id：{}".format(task_name, (end - start), os.getpid()))
    except BaseException as e:
        print(e)


if __name__ == '__main__':
    # 和主进程同生共死
    pool = Pool(5)
    tasks = ['听音乐', '吃饭', '打游戏', '散步', '做饭', '看孩子', '看电视']
    for t in tasks:
        # 用的是非阻塞模式
        pool.apply(task, args=(t,))
    pool.close()  # 添加任务结束
    pool.join()  # 防止主进程结束
    print('over!!!!!!')
