# 打开文件
# open(path, flag[, encoding][, errors])
# path: 要打开文件的路径
# flag: 打开方式
#
# r: ️只读的方式打开文件，文件的描述符放在开头
# rb: 以二进制的打开一个文件用于只读，文件的描述符放在开头
# r+: 打开一个文件用于读写，文件的描述符放在文件的开头
# w: 打开一个文件只用于写入，如果文件存在就会覆盖，如果不存在就会创建新的文件
# wb: 打开一个文件只用于写入二进制文件，如果文件存在就会覆盖，如果不存在就会创建新的文件
# a: 打开一个文件用于追加，如果文件存在，文件描述符会放在末尾
# a+:
# eroding:
# errors:
path = "/Users/yangshuai/PycharmProjects/demo/file.txt"
f = open(path, "r", encoding="utf-8", errors="ignoe")

# 读取内容

# 读取所有
# str1 = f.read()
# print(str1)

# 按字符数读取
# str2 = f.read(10)
# print(str2)

# 读取整行，包含"\n"字符
# str3 = f.readline()
# print(str3)

# 还是读取具体的字符数
# str4 = f.readline(10)
# print(str4)

# 读取所有行，返回列表
# list5 = f.readlines()
# print(list5)

# 给定的数字大于0，返回世纪size字节的行数
# list6 = f.readlines(10)
# print(list6)

# 关闭文件
f.close()

# 这样就不用使用try finally来关闭文件了
with open(path, "r", encoding="utf-8", errors="ignoe") as f:
    print(f.readlines())
