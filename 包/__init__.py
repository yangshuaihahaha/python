# 包是一个分层次的文件目录结构，它定义了一个由模块及子包，和子包下的子包等组成的 Python 的应用环境。
#
# 简单来说，包就是文件夹，但该文件夹下必须存在 match和search函数.py 文件, 该文件的内容可以为空。match和search函数.py 用于标识当前文件夹是一个包。
if __name__ == '__main__':
    print ('作为主程序运行')
else:
    print ('package_runoob 初始化')