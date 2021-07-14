import sys
from collections import deque
sys.stdin = open('input.txt')
input = sys.stdin.readline

y = (-1,0,1,0)
x = (0,1,0,-1)
direct = [(dy,dx) for dy,dx in zip(y,x)]
R,C = map(int,input().rstrip().split())
board = [input().rstrip() for _ in range(R)]
q = deque([(0,0,board[0][0])])
res = 1

while q:
    i,j,visited = q.popleft()
    for d in direct:
        ny = i+d[0]
        nx = j+d[1]
        if 0<=ny<R and 0<=nx<C and board[ny][nx] not in visited:
            q.append((ny,nx,visited+board[ny][nx]))
            res = max(res,len(visited)+1)

print(res)
