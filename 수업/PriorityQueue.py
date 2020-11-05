from queue import PriorityQueue

q = PriorityQueue(maxsize=4)

q.put(4)
q.put(1)
q.put(7)
q.put(3)

print('q: {}'.format(q.qsize()))
print(q.full())

for i in range(5):
    print(q.full())
    if not q.empty():
        print(q.get())

print(q.qsize())

print('hi')