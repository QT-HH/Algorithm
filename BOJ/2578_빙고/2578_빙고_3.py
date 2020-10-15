import sys
sys.stdin = open('input.txt')

def bingo():
    cnt = 0
    for i in range(5):
        tmp = 0
        for j in range(5):
            tmp += check[i][j]
        if tmp == 5:
            cnt += 1
    for i in range(5):
        tmp = 0
        for j in range(5):
            tmp += check[j][i]
        if tmp == 5:
            cnt += 1
    tmp = 0
    for i in range(5):
        tmp += check[i][i]
    if tmp == 5:
        cnt += 1
    tmp = 0
    for i in range(5):
        tmp += check[4-i][i]
    if tmp == 5:
        cnt += 1
    if cnt >= 3:
        return True
    else:
        return False
bingo_board = []
num = []
for _ in range(5):
    bingo_board += list(map(int, input().split()))

for _ in range(5):
    num += list(map(int, input().split()))
check = [[0]*5 for _ in range(5)]

for i in range(25):
    idx = bingo_board.index(num[i])
    row, col = idx//5, idx%5
    check[row][col] = 1
    if bingo():
        break
print(i+1)