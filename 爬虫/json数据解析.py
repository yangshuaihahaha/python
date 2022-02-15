import json
# import demjson

data = [{'a': None, 'b': 2, 'c': 3, 'd': 4, 'e': 5}]

output = json.dumps(data)
print(json)
# 使用参数让json数据格式化输出
output1 = json.dumps({'a': 'Runoob', 'b': 7}, sort_keys=True, indent=4, separators=(',', ': '))
print(output1)

# python 原始类型向 json 类型的转化对照表：
# dict	object
# list, tuple	array
# str, unicode	string
# int, long, float	number
# True	true
# False	false
# None	null

# json.loads
# json.loads 用于解码 JSON 数据。该函数返回 Python 字段的数据类型。
# 以下实例展示了Python 如何解码 JSON 对象：
jsonData = '{"a":1,"b":2,"c":3,"d":4,"e":5}';

text = json.loads(jsonData)
print(text)
# json 类型转换到 python 的类型对照表：
# object	dict
# array	list
# string	unicode
# number (int)	int, long
# number (real)	float
# true	True
# false	False
# null	None

#
# data = [{'a': 1, 'b': 2, 'c': 3, 'd': 4, 'e': 5}]
# json = demjson.encode(data)
# print(json)
#
# json = '{"a":1,"b":2,"c":3,"d":4,"e":5}';
# text = demjson.decode(json)
# print(text)
