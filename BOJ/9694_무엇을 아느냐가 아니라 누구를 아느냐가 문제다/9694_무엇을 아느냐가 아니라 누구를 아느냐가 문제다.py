import sys
sys.stdin = open('input.txt')

import heapq

def dijkstra(graph, start, X):
    distance = [INF] * X
    distance[start] = 0
    q = []
    heapq.heappush(q, (0,start))
    path = [-1 for _ in range(X)]

    while q:
        dist, now = heapq.heappop(q)
        if distance[now] < dist:
            continue
        for i in graph[now]:
            cost = dist + i[1]
            if cost < distance[i[0]]:
                distance[i[0]] = cost
                path[i[0]] = now
                heapq.heappush(q, (cost, i[0]))

    return path

T = int(sys.stdin.readline().rstrip())
for t in range(1,T+1):
    N,M = map(int,sys.stdin.readline().rstrip().split())

    relation = [[] for _ in range(M)]
    for _ in range(N):
        x,y,z = map(int,sys.stdin.readline().rstrip().split())
        relation[x].append((y, z))
        relation[y].append((x, z))

    INF = float('inf')
    res = dijkstra(relation, 0, M)
    if res[-1] == -1:
        print('Case #{}: -1'.format(t))
    else:
        result = [M-1]
        while result[-1]:
            go = res[result[-1]]
            result.append(go)
        result = ' '.join(map(str,reversed(result)))
        print('Case #{}: {}'.format(t,result))

