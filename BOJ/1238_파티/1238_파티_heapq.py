import sys
sys.stdin = open('input.txt')

import heapq
INF = float('inf')
def dijkstra(graph, start, N):
    distance = [INF] * (N+1)
    distance[start] = 0
    q = []
    heapq.heappush(q, (0,start))

    while q:
        dist, now = heapq.heappop(q)
        if distance[now] < dist:
            continue
        for i in graph[now]:
            cost = dist + i[1]
            if cost < distance[i[0]]:
                distance[i[0]] = cost
                heapq.heappush(q, (cost,i[0]))

    return distance

N,M,X = map(int,sys.stdin.readline().rstrip().split())
board = [[] for _ in range(N+1)]
rev_board = [[] for _ in range(N+1)]

for _ in range(M):
    i,j,T = map(int,sys.stdin.readline().rstrip().split())
    board[i].append((j,T))
    rev_board[j].append((i,T))


go_out = dijkstra(board, X, N)
come = dijkstra(rev_board, X, N)
res = 0
for i in range(1,N+1):
    res = max(res, go_out[i]+come[i])

print(res)
