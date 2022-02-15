a = 1
if a == 1:
    print(1)
elif a == 2:
    print(2)
else:
    print(3)

b = 1
while b <= 3:
    print("I am is a good man")
    b += 1
else:
    print("very very good man")

list = [1, 2, 3, 4, 5, 6]
for val in list:
    print(val)

# range(start, end, step) 列表生成器，生成列表函数
for val in range(10):
    print(val)
for val in range(2, 20, 2):
    print(val)
# 获取下标
for index, m in enumerate([1, 2, 3, 4, 5, 6]):
    print(index, m)

# break语句，跳出for和while的循环

