# 创建空元组
tuple1 = ()
# 创建带有数据的元组
tuple2 = (1, 2, 3, 4, "good", 5)
print(tuple2)
# 创建只有一个数据的元组
tuple3 = (1,)  # 必须加逗号，否则创建的是数字1
print(tuple3)
# 获取元组
tuple3 = (1, 2, 3, 4, 5, 6)
print(tuple3[0])
# 获取最后一个元素
print(tuple3[-1])
print(tuple3[-2])
# 修改元组
tuple4 = (1, 2, 3, 4, 5, 6)
# tuple1[2] = 100 会报错，一旦创建，不能修改
tuple5 = (1, 2, 3, 4, [5, 6, 7])
# tuple5[-1] = [1, 2, 3] 这样就会报错，元组不能改变
tuple5[-1][0] = 500  # 这样不会报错
print(tuple5)
# 创建元组的另一种方法
tuple6 = "a", "b", "c", "d"
print(tuple6)
# 访问部分数据
tuple7 = (1, 2, 3, 4, 5, 6)
print(tuple7[1:])
print(tuple7[:5])
print(tuple7[1:5])
# 元组的运算符
tuple8 = (1, 2, 3)
tuple9 = ("a", "b", "c")
tuple10 = tuple8 + tuple9
print(tuple10)

print(len(tuple10))

print(tuple10 * 4)

print(1 in tuple10)

for val in tuple10:
    print(val)

print(max(tuple6))

print(min(tuple6))
# 转为数组
print(tuple(tuple7))

