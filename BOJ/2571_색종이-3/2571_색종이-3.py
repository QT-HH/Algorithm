import sys
sys.stdin=open('input.txt')

n = int(input())
board=[[0]*100 for _ in range(100)]
for _ in range(n):
    r,c = map(int,input().split())
    for i in range(c,c+10):
        for j in range(r,r+10):
            board[i][j]=1

for i in range(1,100):
    for j in range(100):
        if board[i][j]:
            board[i][j]+=board[i-1][j]

res = 0
for j in range(99):
    for i in range(100):
        if board[i][j]:
            height = board[i][j]
            k=0
            while j+k<100 and board[i][j+k]:
                height = min(height,board[i][j+k])
                k+=1
                if res < height*k:
                    res = height*k

print(res)
