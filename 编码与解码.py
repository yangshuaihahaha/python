# 编码
path = "/Users/yangshuai/PycharmProjects/demo/file.txt"
with open(path, "wb") as f1:
    str = "sunck is a good man"
    f1.write(str.encode("utf-8"))

with open(path, "rb") as f2:
    data = f2.read()
    print(data)
    print(type(data))
    newData = data.decode("utf-8")
    print(newData)
    print(type(newData))
