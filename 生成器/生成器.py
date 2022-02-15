def gen():
    n = 0
    while True:
        yield n
        n += 1


g = gen()
print(g)  # <generator object gen at 0x00000246E165A7C8>
print(next(g))  # 输出结果为0
print(next(g))  # 输出结果为1


def func():
    yield from "ABC"


for x in func():
    print(x)

L = [x for x in range(10)]
print(L)

G = (x for x in range(10))
# print(G.__next__())
# print(G.__next__())
# print(G.__next__())
# print(G.__next__())
# print(G.__next__())
# print(G.__next__())
# print(G.__next__())
# print(G.__next__())
# print(G.__next__())
# print(G.__next__())

for n in range(10):
    print(G.__next__())

# for n in G:
#     print(n)
