# dir() 函数一个排好序的字符串列表，内容是一个模块里定义过的名字。
#
# 返回的列表容纳了在一个模块里定义的所有模块，变量和函数。如下一个简单的实例：
import math

content = dir(math)

print(content)
