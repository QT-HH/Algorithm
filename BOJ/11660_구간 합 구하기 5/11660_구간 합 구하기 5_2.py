import sys
sys.stdin = open('input.txt')

def getNum(i):
    return int(i)-1

N,M = map(int,input().split())
board = [list(map(int,input().split())) for _ in range(N)]

for i in range(N):
    for j in range(1,N):
        board[i][j] += board[i][j-1]

for i in range(N):
    for j in range(1,N):
        board[j][i] += board[j-1][i]


find_idx = [list(map(getNum,sys.stdin.readline().split())) for _ in range(M)]

for y1, x1, y2, x2 in find_idx:

    result = board[y2][x2]
    if y1 > 0:
        result -= board[y1-1][x2]
    if x1 > 0:
        result -= board[y2][x1-1]
    if x1 > 0 and y1 > 0:
        result += board[y1-1][x1-1]
    print(result)