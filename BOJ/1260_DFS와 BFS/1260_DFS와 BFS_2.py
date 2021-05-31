import sys
from collections import deque

def dfs(s):
    ans = []
    stack = [s]
    visited = set()

    while stack:
        now = stack.pop()
        if now in visited:
            continue
        else:
            stack.extend(graph[now])
            visited.add(now)
            ans.append(now)
    print(*ans)

def bfs(s):
    ans = []
    q = deque([s])
    visited = set()

    while q:
        now = q.popleft()
        if now in visited:
            continue
        else:
            q.extend(reversed(graph[now]))
            visited.add(now)
            ans.append(now)
    print(*ans)

N,M,V = map(int,sys.stdin.readline().strip().split())
graph = [[] for _ in range(N+1)]

for t in range(M):
    x,y = map(int,sys.stdin.readline().strip().split())
    graph[x].append(y)
    graph[y].append(x)

for i in graph:
    i.sort(reverse=True)

dfs(V)
bfs(V)
