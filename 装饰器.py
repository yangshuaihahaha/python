# 概念
# 是一个闭包，把一个函数当作参数返回一个替代版的参数，本质上就是一个返回函数的函数
def func1():
    print("I am a good man")


def outer(func):
    def inner():
        print("*********")
        func()

    return inner


f = outer(func1)
f()


def decorator(func):
    def inner(age1):
        if age1 < 0:
            age1 = 0
        func(age1)

    return inner


@decorator
def say(age):
    print("I am %d years old" % (age))


# 通用装饰器
def decorator2(func):
    def inner(*values, **keywords):
        print("*********")
        func(*values, **keywords)

    return inner


@decorator2
def say(age, name):
    print("I am %d years old" % (age))
    print("My name is %s" % (name))


@decorator2
def say2(keywords):
    print(keywords)


say2({"name": "tom"})
