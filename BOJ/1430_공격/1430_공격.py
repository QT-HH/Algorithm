import sys
from collections import deque
sys.stdin = open('input.txt')
input = sys.stdin.readline

def bfs(t, R, D, towers, X, Y):
    visited = set()
    visited.add(t)
    t = list(t)
    t.append(D)
    t = tuple(t)
    q = deque([t])

    while q:
        now = q.popleft()
        for tower in towers:
            ny = abs(tower[0] - now[0])
            nx = abs(tower[1] - now[1])
            if ny+nx <= R and tower not in visited:
                if abs(tower[0]-Y) + abs(tower[1]-X) <= R:
                    return now[2]*0.5
                else:
                    q.append((tower[0], tower[1], now[2]*0.5))
                    visited.add(tower)

    return 0

N,R,D,X,Y = map(int,input().rstrip().split())
towers = set()
for _ in range(N):
    tx, ty = map(int,input().rstrip().split())
    towers.add((ty, tx))

res = 0
for t in towers:
    if abs(t[0]-Y) + abs(t[1]-X) <= R:
        res += D
    else:
        res += bfs(t, R, D, towers, X, Y)

print(round(res,3))