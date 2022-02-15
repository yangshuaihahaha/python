# 键一般是唯一的，如果重复最后一个键值会替换前面的，值不需要唯一
dict1 = {1: 2, 3: 4, 1: 6}
print(dict1)
print(dict1[1])

dict2 = {'Alice': '2341', 'Beth': '9102', 'Cecil': '3258'}
print(dict2)
print(dict2["Alice"])

# 更新
dict3 = {'Name': 'Zara', 'Age': 7, 'Class': 'First'}
# 更新
dict3["Age"] = 8
# 添加
dict3["School"] = "RUN"
print(dict3)
# 删除
dict4 = {'Name': 'Zara', 'Age': 7, 'Class': 'First'}
del dict4["Name"]
print(dict4)
# 键必须不可变，所以可以用数字，字符串或元组充当，用列表就不行
dict5 = {(1, 2, 3): 'Zara'}
print(dict5)
# dict6 = {[1, 2, 3]: 'Zara'} # 会报错

# 字典的一些内置函数和方法
dict7 = {(1, 2, 3): 'Zara'}
print(len(dict7))
print(str(dict7))
print(type(dict7))
# 返回一个浅复制
print(dict7.copy())
# 删除所有元素
dict7.clear()
print(dict7)
# seq -- 字典键值列表。
# value -- 可选参数, 设置键序列（seq）的值。
seq = ('Google', 'Runoob', 'Taobao')
print(dict.fromkeys(seq, 10))
# 判断某个元素是否存在
dict8 = {'Name': 'Zara', 'Age': 7}
print("Name" in dict8)
# 循环遍历
dict = {'Google': 'www.google.com', 'Runoob': 'www.runoob.com', 'taobao': 'www.taobao.com'}
print(dict.items())
for key, values in dict.items():
    print(key, values)

for values in dict.items():
    print(values)
