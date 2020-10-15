import sys
sys.stdin = open('input.txt')

def bingo(i,j):
    if i==j:
        for b in range(5):
            if board[b][b]:
                break
        else:
            cnt[0]+=1

    if i+j==4:
        for b in range(5):
            if board[b][4-b]:
                break
        else:
            cnt[0]+=1

    for b in range(5):
        if board[i][b]:
            break
    else:
        cnt[0]+=1

    for b in range(5):
        if board[b][j]:
            break
    else:
        cnt[0]+=1


def find(x):
    for i in range(5):
        for j in range(5):
            if board[i][j] == x:
                board[i][j] = 0
                bingo(i,j)
                return

def call():
    c = 0
    for i in range(5):
        for j in range(5):
            c+=1
            find(num[i][j])
            if cnt[0]>=3:
                return c

board = [list(map(int,input().split())) for _ in range(5)]
num = [list(map(int,input().split())) for _ in range(5)]
cnt = [0]
print(call())
