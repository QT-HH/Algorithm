# 1 2 1 3 2 4 2 5 4 6 5 6 6 7 3 7
import collections

data = list(map(int, input().split()))

nodes = [[] for _ in range(8)]
for i in range(0, len(data) - 1, 2):
    nodes[data[i]].append(data[i + 1])
    nodes[data[i + 1]].append(data[i])

q = collections.deque()
q.append(1)
rode = []

while q:
    now = q.popleft()
    if now not in rode:
        rode.append(now)
        q.extend(nodes[now])

print(rode)

