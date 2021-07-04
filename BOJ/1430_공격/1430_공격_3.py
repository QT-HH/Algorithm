import sys
from collections import deque
sys.stdin = open('input.txt')
input = sys.stdin.readline

def bfs(t, R, D, X, Y, towers):
    if (t[0]-Y)*(t[0]-Y) + (t[1]-X)*(t[1]-X) <= R*R:
        return D

    visited = set()
    visited.add(t)
    t = list(t)
    t.append(D)
    q = deque([t])

    while q:
        now = q.popleft()
        for i in towers[(now[0], now[1])]:
            if i not in visited:
                if (i[0]-Y)*(i[0]-Y) + (i[1]-X)*(i[1]-X) <= R*R:
                    return now[2] * 0.5
                else:
                    visited.add(i)
                    q.append((i[0], i[1], now[2]*0.5))

    return 0


N,R,D,X,Y = map(int,input().rstrip().split())
towers = dict()
for _ in range(N):
    tx, ty = map(int,input().rstrip().split())
    towers[(ty, tx)] = []

t_list = list(towers)
for i in range(N):
    for j in range(i+1,N):
        dy = t_list[i][0]-t_list[j][0]
        dx = t_list[i][1]-t_list[j][1]
        if dy*dy + dx*dx <= R*R:
            towers[t_list[i]].append(t_list[j])
            towers[t_list[j]].append(t_list[i])

res = 0
for t in towers:
    res += bfs(t, R, D, X, Y, towers)

print(round(res,2))
