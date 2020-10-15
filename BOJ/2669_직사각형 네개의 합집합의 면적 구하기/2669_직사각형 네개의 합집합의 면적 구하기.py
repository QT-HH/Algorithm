import sys
sys.stdin = open('input.txt')

squares = [list(map(int,input().split())) for _ in range(4)]
board = [[0]*100 for _ in range(100)]

for s in range(4):
    x1,y1,x2,y2 = squares[s]
    for i in range(y1-1,y2-1):
        for j in range(x1-1,x2-1):
            board[i][j] = 1

res = 0
for i in range(100):
    for j in range(100):
        res+=board[i][j]

print(res)