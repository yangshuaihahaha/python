path = "/Users/yangshuai/PycharmProjects/demo/file.txt"
f = open(path, "a")
# 将信息写入缓冲区
f.write("hahaha")

# 刷新缓冲区, 立即写入文件，而不是被动的等待自动刷新
f.flush()

# 关闭
f.close()