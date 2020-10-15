import sys
sys.stdin = open('input.txt')

N = int(input())
data = [tuple(map(int,input().split())) for _ in range(N)]
board = [[0]*100 for _ in range(100)]
for d in data:
    for j in range(d[0],d[0]+10):
        for i in range(d[1],d[1]+10):
            board[i][j] = 1

di = [-1,0,1,0]
dj = [0,1,0,-1]
direct = [d for d in zip(di,dj)]
cnt=0
for i in range(100):
    for j in range(100):
        for d in direct:
            a = i+d[0]
            b = j+d[1]
            if 0<=a<100 and 0<=b<100:
                if board[i][j] and not board[a][b]:
                    cnt+=1
        if (i==0 or i==99) and board[i][j]:
            cnt+=1
        if (j==0 or j==99) and board[i][j]:
            cnt+=1

print(cnt)
