import sys
sys.stdin = open('input.txt')

N = int(input())
board = [[0]*100 for _ in range(100)]
for _ in range(N):
    x,y = map(int,input().split())
    for i in range(y,y+10):
        for j in range(x,x+10):
            if 0<=i<100 and 0<=j<100:
                board[i][j] = 1

print(sum(sum(x) for x in board))