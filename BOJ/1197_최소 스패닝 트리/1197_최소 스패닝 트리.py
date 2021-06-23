import sys
import heapq
sys.stdin = open('input.txt')
input = sys.stdin.readline
INF = float('inf')

def prim(start):
    dist = [INF] * V
    visited = [False] * V
    q = []
    heapq.heappush(q, (0,start))

    while q:
        now = heapq.heappop(q)
        if not visited[now[1]]:
            visited[now[1]] = True
            dist[now[1]] = now[0]
            for i in nodes[now[1]]:
                heapq.heappush(q, i)

    return sum(dist)

V,E = map(int,input().rstrip().split())
nodes = [[] for _ in range(V)]
for _ in range(E):
    A,B,C = map(int,input().rstrip().split())
    A -= 1
    B -= 1
    nodes[A].append((C,B))
    nodes[B].append((C,A))

print(prim(0))
