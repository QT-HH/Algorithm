# 1 2 1 3 2 4 2 5 4 6 5 6 6 7 3 7

data = list(map(int, input().split()))

nodes = [[] for _ in range(8)]
for i in range(0, len(data) - 1, 2):
    nodes[data[i]].append(data[i + 1])
    nodes[data[i + 1]].append(data[i])

stack = [1]
rode = []

while stack:
    now = stack.pop()
    if now not in rode:
        rode.append(now)
        stack.extend(nodes[now])

print(rode)
