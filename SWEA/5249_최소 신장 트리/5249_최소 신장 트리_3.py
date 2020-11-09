import sys
sys.stdin = open('input.txt')

from heapq import *

def prim(x):
    q = [[0,x]]
    while q:
        now = heappop(q)
        if not visited[now[1]]:
            visited[now[1]] = True
            path[now[1]] =now[0]
            for i in nodes[now[1]]:
                heappush(q,i)

T = int(input())
for t in range(1,T+1):
    V,E = map(int,input().split())

    nodes = {}
    visited = [False]*(V+1)
    path = [11]*(V+1)
    path[0] = 0

    for i in range(E):
        a,b,c = map(int,input().split())
        if nodes.get(a):
            nodes[a].append([c,b])
        else:
            nodes[a] = [[c,b]]
        if nodes.get(b):
            nodes[b].append([c,a])
        else:
            nodes[b] = [[c,a]]

    # print(nodes)
    prim(0)
    print('#{} {}'.format(t,sum(path)))