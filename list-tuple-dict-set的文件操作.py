import pickle

# 写入
myList = [1, 2, 3, 4, 5, 6, "hahah"]
path = "/Users/yangshuai/PycharmProjects/demo/file.txt"
f = open(path, "wb")
pickle.dump(myList, f)

# 读取
f = open(path, "rb")
myList1 = pickle.load(f)
print(myList1)
