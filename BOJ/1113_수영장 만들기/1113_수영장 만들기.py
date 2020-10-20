import sys
sys.stdin = open('input.txt')

from collections import deque

def find(h):
    global N,M
    res = 0
    visited_n = set()
    for i in range(1,N-1):
        for j in range(1,M-1):
            if (i,j) in visited or (i,j) in visited_n:
                continue
            elif ground[i][j] < h:
                visited_tmp = {(i,j)}
                hole = True
                q = deque()
                q.append((i,j))
                while q:
                    t = q.popleft()

                    for d in direct:
                        y = t[0]+d[0]
                        x = t[1]+d[1]
                        if 0<=x<M and 0<=y<N:
                            if ground[y][x] >= h or (y,x) in visited_tmp:
                                continue

                            if x == 0 or x == M-1 or y == 0 or y == N-1:
                                hole = False
                            visited_tmp.add((y,x))
                            q.append((y,x))

                visited_n.update(visited_tmp)
                if hole:
                    visited.update(visited_tmp)
                    for a in visited_tmp:
                        res += (h - ground[a[0]][a[1]])

    return res


d_i = [-1,0,1,0]
d_j = [0,1,0,-1]
direct = [ d for d in zip(d_i,d_j)]

N,M = map(int,input().split())
ground = [list(map(int,' '.join(input()).split())) for _ in range(N)]

max_g = 0
for g in ground:
    x = max(g)
    if max_g < x:
        max_g = x

visited = set()
result = 0
for h in range(max_g,0,-1):
    result += find(h)

print(result)
