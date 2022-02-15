# 一个 Python 表达式可以访问局部命名空间和全局命名空间里的变量。如果一个局部变量和一个全局变量重名，则局部变量会覆盖全局变量。
#
# 每个函数都有自己的命名空间。类的方法的作用域规则和通常函数的一样。
#
# Python 会智能地猜测一个变量是局部的还是全局的，它假设任何在函数内赋值的变量都是局部的。
#
# 因此，如果要给函数内的全局变量赋值，必须使用 global 语句。
#
# global VarName 的表达式会告诉 Python， VarName 是一个全局变量，这样 Python 就不会在局部命名空间里寻找这个变量了。
#
# 例如，我们在全局命名空间里定义一个变量 Money。我们再在函数内给变量 Money 赋值，然后 Python 会假定 Money 是一个局部变量。然而，我们并没有在访问前声明一个局部变量 Money，结果就是会出现一个 UnboundLocalError 的错误。取消 global 语句前的注释符就能解决这个问题。
Money = 2000


def AddMoney():
    global Money
    Money = Money + 1


print(Money)
AddMoney()
print(Money)
