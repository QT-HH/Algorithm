import sys
sys.stdin = open('input.txt')

def dfs(i,j):
    stack = [(i,j)]
    while stack:
        p,q = stack.pop()
        for d in direct:
            y = p+d[0]
            x = q+d[1]
            if 0 <= y <R and 0<= x <C and not check[y][x]:
                check[y][x] = True
                if board[y][x] == '#':
                    stack.append((y,x))

direct = [(-1,0),(0,1),(1,0),(0,-1)]

R,C = map(int,input().split())
board = []
check = [[False]*C for _ in range(R)]
cnt = 0

for _ in range(R):
    board.append(sys.stdin.readline())

for i in range(R):
    for j in range(C):
        if board[i][j] == '#' and not check[i][j]:
            dfs(i,j)
            cnt += 1

print(cnt)