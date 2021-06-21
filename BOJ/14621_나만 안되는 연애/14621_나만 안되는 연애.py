import sys
sys.stdin = open('input.txt')
import heapq
input = sys.stdin.readline
INF = float('inf')

def prim(start):
    dist = [INF] * N
    visited = [False] * N
    q = []
    heapq.heappush(q,(0,start))

    while q:
        now = heapq.heappop(q)
        if not visited[now[1]]:
            visited[now[1]] = True
            dist[now[1]] = now[0]
            for i in nodes[now[1]]:
                heapq.heappush(q,i)

    for j in dist:
        if j == float('inf'):
            return -1
    return sum(dist)

N,M = map(int,input().rstrip().split())
gen = input().rstrip().split()
nodes = [[] for _ in range(N)]
for _ in range(M):
    u,v,d = map(int,input().rstrip().split())
    u -= 1
    v -= 1
    if gen[u] != gen[v]:
        nodes[u].append((d,v))
        nodes[v].append((d,u))


print(prim(0))
