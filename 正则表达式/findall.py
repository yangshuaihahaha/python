# 在字符串中找到正则表达式所匹配的所有子串，并返回一个列表，如果没有找到匹配的，则返回空列表。
# 注意： match 和 search 是匹配一次 findall 匹配所有。
# re.findall(string[, pos[, endpos]])
# string 待匹配的字符串。
# pos 可选参数，指定字符串的起始位置，默认为 0。
# endpos 可选参数，指定字符串的结束位置，默认为字符串的长度。
import re

pattern = re.compile(r'\d+')  # 查找数字
result1 = pattern.findall('runoob 123 google 456')
result2 = pattern.findall('run88oob123google456', 0, 10)

print(result1)
print(result2)

# finditer
it = re.finditer(r"\d+", "12a32bc43jf3")
for match in it:
    print("finditer", match.group())

# re.split
# split 方法按照能够匹配的子串将字符串分割后返回列表，它的使用形式如下：
print(re.split('\W+', 'runoob, runoob, runoob.'))
print(re.split('(\W+)', ' runoob, runoob, runoob.')) #包括自身
print(re.split('\W+', ' runoob, runoob, runoob.', 1))
