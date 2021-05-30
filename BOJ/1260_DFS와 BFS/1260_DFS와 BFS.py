import sys
sys.stdin = open('input.txt')

from collections import deque

def dfs(s):
    ans = []
    stack = [s]
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
    while q:
        now = q.popleft()
        if now in visited:
            continue
        else:
            q.extend(reversed(graph[now]))
            visited.add(now)
            ans.append(now)
    print(*ans)

N,M,V = map(int,input().split())
graph = dict()
visited = set()

for t in range(M):
    x,y = map(int,sys.stdin.readline().strip().split())
    if graph.get(x):
        graph[x].append(y)
    else:
        graph[x] = [y]

    if graph.get(y):
        graph[y].append(x)
    else:
        graph[y] = [x]

for i in graph:
    graph[i].sort(reverse=True)

if graph.get(V):
    dfs(V)
    visited = set()
    bfs(V)
else:
    print(V)
    print(V)