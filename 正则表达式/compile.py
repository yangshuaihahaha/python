# compile 函数
# compile 函数用于编译正则表达式，生成一个正则表达式（ Pattern ）对象，供 match() 和 search() 这两个函数使用。
# re.compile(pattern[, flags])
# pattern : 一个字符串形式的正则表达式
# flags 可选，表示匹配模式，比如忽略大小写，多行模式等，具体参数为：
# re.I 忽略大小写
# re.L 表示特殊字符集 \w, \W, \b, \B, \s, \S 依赖于当前环境
# re.M 多行模式
# re.S 即为' . '并且包括换行符在内的任意字符（' . '不包括换行符）
# re.U 表示特殊字符集 \w, \W, \b, \B, \d, \D, \s, \S 依赖于 Unicode 字符属性数据库
# re.X 为了增加可读性，忽略空格和' # '后面的注释
import re

pattern = re.compile(r'\d+')  # 用于匹配至少一个数字
m = pattern.match('one12twothree34four')  # 查找头部，没有匹配
print("查找头部，没有匹配", m)
m = pattern.match('one12twothree34four', 2, 10)  # 从'e'的位置开始匹配，没有匹配
print("从'e'的位置开始匹配，没有匹配", m)
m = pattern.match('one12twothree34four', 3, 10)  # 从'1'的位置开始匹配，正好匹配
print("从'1'的位置开始匹配，正好匹配", m)  # 返回一个 Match 对象
print("group(0)", m.group(0))  # 可省略 0
print("start(0)", m.start(0))  # 可省略 0
print("end(0)", m.end(0))  # 可省略 0
print("span(0)", m.span(0))  # 可省略 0

