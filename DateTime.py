import datetime

# datetime比time高级了不少

# 模块中的类
# datetime 同时有时间和日期
# timedelta 计算时间的跨度
# tzinfo 时区相关
# time 只关注时间
# date 只关注日期


d1 = datetime.datetime.now()
print(d1)

# 获取指定的时间
d2 = datetime.datetime(1999, 10, 1, 10, 29, 25, 123)
print(d2)

# 时间转为字符串
d3 = d1.strftime("%Y-%m-%d %X")
print(d3)

# 将格式化字符串转为datetime对象
# 注意：转换的格式要跟字符串一致
d4 = datetime.datetime.strptime(d3, "%Y-%m-%d %X")
print(d4)

d5 = datetime.datetime(1999, 10, 1, 10, 29, 25, 123)
d6 = datetime.datetime.now()
d7 = d6 - d5
# 7474 days, 23:15:53.893717
print(d7)
print(d7.days)
print(d7.seconds) #间隔天数除外的秒数


