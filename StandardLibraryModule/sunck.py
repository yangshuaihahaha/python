# 每一个模块都有一个__name__属性，当其值等于__main__时，表明该模块自身在执行
if __name__ == "__main__":
    print("这是sunck.py")
else:
    print(__name__)
    def sayGood():
        print("good")


    def sayHello():
        print("hello")


    def sayBybe():
        print("Bybe")

it = '123'
IT = '456'
