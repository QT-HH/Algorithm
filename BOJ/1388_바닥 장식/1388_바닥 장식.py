import sys
sys.stdin = open('input.txt')
input = sys.stdin.readline

N,M = map(int,input().rstrip().split())
pan = {'|': (1, 0), '-': (0, 1)}
board = [input().rstrip() for _ in range(N)]
visited = set()

res = 0
for i in range(N):
    for j in range(M):
        if (i,j) not in visited:
            match = board[i][j]
            now = (i, j)
            visited.add((i, j))
            d = pan[board[i][j]]
            while True:
                y = now[0] + d[0]
                x = now[1] + d[1]
                if 0<=y<N and 0<=x<M and board[y][x] == match and (y,x) not in visited:
                    visited.add((y, x))
                    now = (y,x)
                else:
                    break
            res += 1

print(res)

