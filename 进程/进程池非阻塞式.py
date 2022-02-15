import os
from multiprocessing import Pool
import time
from random import random


# 非阻塞式
# 全部添加到队列中，立刻返回，并没有等待其他的进程完毕之后，但是回掉函数是等待任务完成之后才调用
def task(task_name):
    try:
        duration = random() * 3
        print(duration)
        print("开始做任务了", task_name)
        start = time.time()

        time.sleep(duration)

        end = time.time()
        return "完成任务{}，用时: {}, 进程id：{}".format(task_name, (end - start), os.getpid())
    except BaseException as e:
        print(e)


def callback_func(n):
    print(n)


if __name__ == '__main__':
    # 和主进程同生共死
    pool = Pool(5)
    tasks = ['听音乐', '吃饭', '打游戏', '散步', '做饭', '看孩子', '看电视']
    for t in tasks:
        # 用的是非阻塞模式
        pool.apply_async(task, args=(t,), callback=callback_func)
    pool.close()  # 添加任务结束
    pool.join()  # 防止主进程结束
    print('over!!!!!!')

# 阻塞式
