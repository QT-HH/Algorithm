import sys
sys.stdin = open('input.txt')

from collections import deque

def bfs():
    visited = set()
    q = deque()
    q.append(1)
    while q:
        now = q.popleft()
        if now in visited:
            continue
        else:
            q.extend(graph[now])
            visited.add(now)
    return len(visited)

com = int(sys.stdin.readline().rstrip())
couples = int(sys.stdin.readline().rstrip())
graph = {}
for _ in range(couples):
    x,y = map(int,sys.stdin.readline().rstrip().split())
    if graph.get(x):
        graph[x].append(y)
    else:
        graph[x] = [y]
    if graph.get(y):
        graph[y].append(x)
    else:
        graph[y] = [x]

print(bfs()-1)