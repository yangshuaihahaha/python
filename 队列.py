import collections

queue = collections.deque()

queue.append("A")
print(queue)
queue.append("B")
print(queue)
queue.append("C")
print(queue)


res1 = queue.popleft()
print(res1)
res2 = queue.popleft()
print(res2)
res3 = queue.popleft()
print(res3)

# res4 = queue.pop()
# print(res4)
# res5 = queue.pop()
# print(res5)
# res6 = queue.pop()
# print(res6)