import sys
sys.stdin = open('input.txt')

N = int(input())
board = [[0]*101 for _ in range(101)]
result = [0]*(N+1)
for n in range(1,N+1):
    x,y,w,h = map(int,input().split())

    for i in range(y,y+h):
        for j in range(x,x+w):
            if 0<=i<=100 and 0<=j<=100:
                board[i][j] = n

for i in range(101):
    for j in range(101):
        result[board[i][j]]+=1

for i in range(1,N+1):
    print(result[i])