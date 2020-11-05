import sys
sys.stdin = open('input.txt')

def dijkstra(start,adj,weight):
    U = {start}
    while len(U) < V:
        min_w = INF
        min_idx = -1
        for i in range(V):
            if i not in U and weight[i] < min_w:
                min_w = weight[i]
                min_idx = i

        U.add(min_idx)
        for i in range(V):
            if i not in U:
                tmp = min_w + adj[min_idx][i]
                if weight[i] > tmp:
                    weight[i] = tmp

    return weight

T = int(input())
for t in range(1,T+1):
    V, E = map(int,input().split())
    V+=1
    INF = float('inf')
    adj = [[INF]*(V) for _ in range(V)]
    for i in range(E):
        s,e,w = map(int,input().split())
        adj[s][e] = w

    start = 0
    weight = adj[start][:]
    result = dijkstra(start,adj,weight)
    print('#{} {}'.format(t,result[-1]))
