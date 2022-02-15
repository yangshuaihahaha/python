try:
    print(3 / 0)
except:
    print("123")
else:
    print("456")
finally:
    print("---")
print("789")

try:
    print(3 / 0)
except BaseException as e:
    print(e)

try:
    print(3 / 0)
except BaseException:
    print("---")

try:
    print(3 / 0)
except BaseException as e:
    print(e)
except ZeroDivisionError as e:
    print(e, 22)


# 断言
def func1(num, div):
    assert (div != 0), "div不能为0"
    return num / div


print(func1(10, 0))
