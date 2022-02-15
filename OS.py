import os

print(os.uname())

print(os.environ())
# 获取当前目录
print(os.curdir())
# 获取当前工作目录，即当前python脚本所在的目录
print(os.getcwd())
# 返回指定目录下的所有文件
print(os.listdir())
# 当前目录下创建新的文件
print(os.mkdir("suck"))
print(os.mkdir(r"/Users/yangshuai/PycharmProjects/demo/file2.txt"))
# 删除
os.rmdir("suck")

# 获取文件属性
print(os.stat("suck"))
# 重命名
os.rename("suck", "kaige")
# 删除普通文件
os.remove("file1.txt")
# 运行shell命令
os.system("mysql.server start")

# os.path里面的方法
# 获取绝对路径
print(os.path.abspath("suck"))
# 拼接路径
p1 = r"/Users/yangshuai/PycharmProjects/demo/"
# 这个路径最前面不能有斜杠
p2 = r"suck"
os.path.join(p1, p2)

# 拆分路径
path2 = r"/Users/yangshuai/PycharmProjects/demo/file.txt"
print(os.path.split(path2))
print(os.path.splitext(path2))

# 判断是否是目录
print(os.path.isdir(path2))

# 判断文件是否存在
print(os.path.isfile(path2))

# 判断目录是否存在
print(os.path.exists(path2))

# 判断文件大小(字节)
print(os.path.getsize(path2))

# 获取文件的目录
print(os.path.dirname(path2))

# 获取文件名
print(os.path.basename(path2))
