import sys
sys.stdin = open('input.txt')
import heapq
input = sys.stdin.readline
INF =  float('inf')

def prim(start, det):
    dist = [INF] * (N+1)
    visited = [False] * (N+1)
    cnt = 0
    q = []
    heapq.heappush(q, (0,start))
    while q:
        if cnt == (N+1):
            break
        now = heapq.heappop(q)
        if not visited[now[1]]:
            visited[now[1]] = True
            cnt += 1
            dist[now[1]] = now[0]
            for i in nodes[now[1]]:
                heapq.heappush(q,(i[0]*det, i[1]))

    res = sum(dist[1:])
    return res*res

N,M = map(int,input().rstrip().split())
nodes = [[] for _ in range(N+1)]
for _ in range(M+1):
    A,B,C = map(int,input().rstrip().split())
    if C:
        C-=1
    else:
        C+=1
    nodes[A].append((C,B))
    nodes[B].append((C,A))

res_min = prim(0,1)
res_max = prim(0,-1)

print(res_max-res_min)