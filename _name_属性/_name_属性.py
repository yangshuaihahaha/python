import sunck
from sunck import sayHello
from sunck import *
from sunck import sayGood, sayHello


# __name__属性
# 模块就是一个可执行的.py文件，一个模块被另一个程序引入，我不想让模块中的某些代码执行
# 可以使用__name__属性来使程序仅调用模块中的一部分

sunck.sayBybe()
print(sunck.it)
sayHello()
