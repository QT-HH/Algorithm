import sys
from collections import deque
sys.stdin = open('input.txt')
input = sys.stdin.readline

def check(y,x,l, visited):
    if 0<=y<l and 0<=x<l and (y,x) not in visited:
        return True
    else:
        return False

def bfs(start, end, l):
    q = deque([start])
    visited = set()
    while q:
        now = q.popleft()
        for d in direct:
            y = now[0]+d[0]
            x = now[1]+d[1]
            if check(y, x, l, visited):
                if y == end[0] and x == end[1]:
                    return now[2]+1
                else:
                    q.append((y,x,now[2]+1))
                    visited.add((y,x))


T = int(input().rstrip())

dy = (2, 1, -1, -2, -2, -1, 1, 2)
dx = (1, 2, 2, 1, -1, -2, -2, -1)
direct = [d for d in zip(dy,dx)]

for t in range(T):
    l = int(input().rstrip())
    ini = [*map(int,input().rstrip().split())]
    des = [*map(int,input().rstrip().split())]

    if ini == des:
        print(0)
    else:
        ini.append(0)
        print(bfs(ini, des, l))





