# -*- coding: utf-8 -*-
import math
import random

# 数学功能
# 返回数据的绝对值

a1 = -10
a2 = abs(a1)
print(a2)

# 比较两个数的大小
a3 = 100
a4 = 9
print(a3 > a4)

# 获取最大值或者最小值
print(max(1, 34, 56, 78))
print(min(2, 34, 6, 8))

# 求x的y次方
print(pow(2, 5))

# 四舍五入
print(round(3.556))
print(round(3.556, 2))

# 使用math库
# 向上取整
print(math.ceil(18.1))
# 向下取整
print(math.floor(18.9))
# 返回整数部分与小数部分
print(math.modf(18.6))
# 开方
print(math.sqrt(16))
# 随机数
print(random.choice([1, 2, 3, 4, 5, 6]))
print(random.choice(range(5)))  # range(5) == [0,1,2,3,4]
print(random.choice("appale"))  # "appale" == ["a", "p", "p", "a", "l", "e"]

# 生成一个1-100之间的随机数
r1 = random.choice(range(100)) + 1
print(r1)

# random.randrange(start, stop, step)
print(random.randrange(1, 100, 2))
# 0-99之间选取一个随机数
print(random.randrange(100))
# 随机选取0-1之间的数
print(random.random())
# 将所有的元素随机排序
list = [1, 2, 3, 4, 5, 6]
random.shuffle(list)
print(list)
# 随机生成一个实数，范围就是[3-9]，两边都包含
print(random.uniform(3, 9))
