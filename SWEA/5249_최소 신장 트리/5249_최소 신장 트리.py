import sys
sys.stdin = open('input.txt')

from queue import PriorityQueue

def prim(n):
    q = PriorityQueue(maxsize=V + 1)
    virtex = [100]*(V+1)
    virtex[n] = 0
    visited = set()
    q.put((0,n))
    while not q.empty():
        now = q.get()
        for i in connect[now[1]]:
            if i == now[1] or i in visited:
                continue
            if virtex[i] > nodes[now[1]][i]:
                virtex[i] = nodes[now[1]][i]
            if now[1] not in visited:
                visited.add(now[1])
            q.put((virtex[i],i))

    result[0] = min(result[0],sum(virtex))



T = int(input())

for t in range(1,T+1):
    V,E = map(int,input().split())

    nodes = [[0]*(V+1) for _ in range(V+1)]

    connect = {}
    for i in range(E):
        x,y,z = map(int,input().split())
        nodes[x][y] = z
        nodes[y][x] = z
        if connect.get(x):
            connect[x].append(y)
        else:
            connect[x] = [y]
        if connect.get(y):
            connect[y].append(x)
        else:
            connect[y] = [x]

    result = [100000]
    prim(0)
    print('#{} {}'.format(t,result[0]))
