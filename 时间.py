# 表示的形式
# 1，时间戳
# 2，元组（year，month，day，hours，miuntes，seconds，weekday，）
# 3，字符串
import time

# 时间戳
c = time.time()
print(c)

# 元组
# 格林尼治时间
t = time.gmtime(c)
print(t)

# 本地时间
b = time.localtime(c)
print(b)

# 将本地元组转成时间戳
m = time.mktime(b)
print(m)

# 将时间元组转成字符串
print(time.asctime(b))

# 将时间戳转为字符串
print(time.ctime(c))

# 转为指定格式的字符串，参数2可以不写
str = time.strftime("%Y-%m-%d %H:%M:%S", b)
print(str)

# 将时间字符串转为时间元组
print(time.strptime(str, "%Y-%m-%d %H:%M:%S"))


# 延迟一个时间，整形或者浮点型

# 返回当前程序的cpu执行时间，可以做性能测试
# Unix始终返回全部的运行时间
# Windows从第二次开始，都是以第一个调用此函数的开始间戳作为基数
time.perf_counter()

time.sleep(2)

y2 = time.perf_counter()
print(y2)

