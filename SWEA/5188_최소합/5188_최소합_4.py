import sys
sys.stdin = open('input.txt')

def dfs(a,b):
    right = down = N*11

    if a == b >= N-1:
        return board[a][b]
    else:
        if a < N-1:
            down = dfs(a+1,b)
        if b < N-1:
            right = dfs(a,b+1)

    if right < down:
        return right + board[a][b]
    else:
        return down + board[a][b]



T = int(input())
for t in range(1,T+1):
    N = int(input())
    board = [list(map(int,input().split())) for _ in range(N)]
    print(dfs(0,0))
