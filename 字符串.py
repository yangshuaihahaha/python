# 重复输出字符串
str9 = "ha"
str10 = str9 * 3
print(str10)

# 访问字符串中的某一个字符
# 通过索引下标查字符，索引从0开始
# 字符串名[下标]
str11 = "Tom is a good man!"
print(str11[0])
# str11[0] = "R" 字符串不可变

# 截取字符串
print(str11[0:3])
print(str11[:3])
print(str11[4:])

# 是否包含某个字符串
print("good" in str11)
print("snuck" not in str11)

# 格式化输出
print("num = %d" % 123)
print("str = %s" % "123")
print("float = %f" % 3.123567999999)
print("float = %.9f" % 3.123567999999)

# 转义字符
# \n 换行
print("身高：\n190")
print('''身高：
177''')

# 如果字符串中好多字符都需要转义，就需要加入很多的\，
# 为了简化python允许r表示内部的字符串默认都不转义
print(r"\\\t\\")

# 将字符串str当成有效的表达式求值并返回结果
print(eval("123"))
print(eval("123 - 1"))
print(eval("123 + 3"))

print(len("Tom is a good man!"))
print("Tom".lower())
print("tom".upper())
print("Tom is a good man!".swapcase())
print("Tom is a good man!".title())

# center(width, fillchar)
# 返回一个指定宽度的居中字符串，fillchar为填充的字符串
str12 = "kaige is anice man"
print(str12.center(30, "*"))

str13 = "kaige is a nice man"
print(str13.ljust(30, "*"))

str13 = "kaige is a nice man"
print(str13.rjust(30, "*"))

# 返回一个长度为width的字符串，原字符串右对齐，前面补0
print("I am a good man".zfill(40))

# 返回字符串中good出现的次数，可以指定范围
print("I am a good man".count("good"))
print("I am a good man".count("good", 15, 30))

# 返回字符串中的位置，可以指定范围
# 如果不存在会返回-1
print("I am a good man".find("man"))
print("I am a good man".find("man", 1, 30))

# 查找字符串的角标，如果不存在会报错
print("I am a good man".index("am"))
print("I am am a good man".rindex("am"))

# 截取字符串左侧指定的字符，默认为空格
print("    I am a good man".lstrip())
print("I am a good man".lstrip("I "))

# 截取字符串右侧指定的字符，默认为空格
print("I am a good man     ".rstrip())
print("I am a good man".rstrip("man"))

# 截取字符串左，右侧指定的字符，默认为空格
print("******I am a good man******".strip("*"))

