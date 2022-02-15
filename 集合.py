# 创建
list1 = [1, 2, 3, 4, 5, 6]
list2 = [1, 2, "hahaha", True]
print(list1)
print(list2)
# 取值
print(list2[1])
# 赋值
list2[1] = 300
print(list2)

# 列表操作
list5 = [1, 2, 3]
list6 = [3, 4, 5]
list7 = list5 + list6
print(list7)

# 列表的重复
list8 = [1, 2, 3]
print(list8 * 3)

# 判断元素是否在列表中
print(2 in list8)

# 列表截取
list10 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print(list10[2:5])
print(list10[3:])
print(list10[:6])

# 二维列表
list11 = [[1, 2, 3, 4, 5, 6], [], ["a", "b", "c"], True]
print(list11)

# 列表方法
# 追加
list12 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
list12.append(11)
# 追加新的元素
list12.append([12, 13, 14])
print(list12)
# 在末尾一次性追加另一个列表中的多个值
list13 = [1, 2, 3, 4, 5]
list13.extend([6, 7, 8])
print(list13)
# 在下标处添加一个元素，不覆盖原来的数据，原数据向后移动
list14 = [1, 2, 3, 4, 5]
list14.insert(1, 100)
print(list14)
# 删除
# pop(x=list[-1]) 移除指定下标处的元素，默认是最后一个
list15 = [1, 2, 3, 4, 5]
list15.pop()
list15.pop(2)
print(list15)
print(list15[-1])
# 移除列表中的某一个元素，根据内容匹配（只会移除第一个匹配的）
list16 = [1, 2, 3, 4, 5, 4]
list16.remove(4)
print(list16)
# 清空
list17 = [1, 2, 3, 4, 5, 6]
list17.clear()
print(list17)
# 找出列表中第一个匹配值的角标，没有就报错
list18 = [1, 26, 38, 1, 52, 6]
print(list18.index(38))
# 指定范围
print(list18.index(38, 1, 3))
# 元素的个数
list20 = [1, 2, 3, 4, 5, 6]
print(len(list20))
# 最大值 最小值
list21 = [1, 2, 3, 4, 5, 6]
print(max(list21))
print(min(list21))
# 元素在列表中出现的次数
list22 = [1, 2, 3, 4, 5, 6, 3, 4, 2, 3, 4, 53, 2]
print(list22.count(3))
# 倒序
list25 = [1, 2, 8, 4, 5, 6]
list25.reverse()
print(list25)
# 排序
list26 = [1, 2, 8, 4, 5, 6]
list26.sort()
print(list26)
# 拷贝
# 浅拷贝（引用拷贝）
list27 = [1, 2, 8, 4, 5, 6]
list28 = list27
list28[2] = 100
print(list27, list28)
# 深拷贝（内存拷贝）
list29 = [1, 2, 8, 4, 5, 6]
list30 = list29.copy()
print(id(list29), id(list30))
# 元组专成列表
print(list((1, 2, 3, 4, 5, 6)))
