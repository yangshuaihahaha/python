import calendar

# 返回指定某年某月的日历
print(calendar.month(2019, 9))
# September 2019
# Mo Tu We Th Fr Sa Su
#                    1
#  2  3  4  5  6  7  8
#  9 10 11 12 13 14 15
# 16 17 18 19 20 21 22
# 23 24 25 26 27 28 29
# 30

# 返回指定年的日历
print(calendar.calendar(2019))

# 判断闰年
print(calendar.isleap(2000))

# 返回某个月的第一天是周几，和这个月所有的天数
print(calendar.monthrange(2017, 7))

# 返回某个月以每一周为元素的列表
print(calendar.monthcalendar(2017, 7))

