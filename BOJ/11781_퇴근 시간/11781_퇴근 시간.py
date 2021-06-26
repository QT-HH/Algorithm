import sys
import heapq
sys.stdin = open('input.txt')
input = sys.stdin.readline
INF = float('inf')

def dijkstra(start, nodes, N, S, E):
    dist = [INF] * N
    dist[0] = 0
    q = []
    heapq.heappush(q, (0, start, 0))

    while q:
        now = heapq.heappop(q)
        if dist[now[1]] < now[0]:
            continue
        for i in nodes[now[1]]:
            cost = now[0] + i[0]
            if i[2]:
                if dist[now[1]] >= E or cost <= S:
                    pass
                else:
                    if dist[now[1]] < S:
                        tmp1 = (S-dist[now[1]])
                        tmp2 = (E - S) * 0.5
                        if i[0] <= tmp1 + tmp2:
                            tmp_t = tmp1 + (i[0]-tmp1)*2
                        else:
                            tmp_t = tmp1 + tmp2*2 + (i[0]-(tmp1+tmp2))
                    else:
                        tmp1 = (E-dist[now[1]])*0.5
                        if i[0] < tmp1:
                            tmp_t = i[0]*2
                        else:
                            tmp_t = tmp1*2 + (i[0]-tmp1)

                    cost = now[0] + tmp_t

            if cost < dist[i[1]]:
                dist[i[1]] = cost
                heapq.heappush(q, (cost, i[1]))

    res = max(dist)
    if res == int(res):
        res = int(res)
    return res


N,M,S,E = map(int,input().rstrip().split())
nodes = [[] for _ in range(N)]
for _ in range(M):
    A,B,L,t1,t2 = map(int,input().rstrip().split())
    A-=1
    B-=1
    nodes[A].append((L,B,t1))
    nodes[B].append((L,A,t2))

print(dijkstra(0, nodes, N, S, E))
