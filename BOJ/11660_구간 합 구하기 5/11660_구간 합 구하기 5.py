import sys
sys.stdin = open('input.txt')

N,M = map(int,input().split())
board = [list(map(int,input().split())) for _ in range(N)]

for i in range(N):
    for j in range(1,N):
        board[i][j] += board[i][j-1]

for i in range(1,N):
    for j in range(N):
        board[i][j] += board[i-1][j]

for i in board:
    print(i)

for _ in range(M):
    y1,x1,y2,x2 = map(lambda x:int(x)-1,input().split())
    cnt=0
    res = board[y2][x2]
    if x2==0 or x1==0:
        pass
    else:
        cnt+=1
        res -= board[y2][x1-1]

    if y2==0 or y1==0:
        pass
    else:
        cnt+=1
        res -= board[y1-1][x2]

    if cnt==2:
        res += board[y1-1][x1-1]

    print(res)