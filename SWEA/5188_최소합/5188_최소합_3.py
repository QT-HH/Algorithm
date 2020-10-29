import sys
sys.stdin = open('input.txt')

def find(row,col):
    print(row,col)
    # 최대값이 N*10 이니까
    down = right = N*11

    #마지막 도달
    if row == col >= N-1:
        return board[row][col]
    # down, right으로 갔을때 cost
    else:
        if row < N-1:
            down = find(row+1,col)
        if col < N-1:
            right = find(row,col+1)

    # 작은 값으로 리턴
    if down < right:
        return down + board[row][col]
    else:
        return right + board[row][col]

T = int(input())
for t in range(1,T+1):
    N = int(input())
    board = [list(map(int,input().split())) for _ in range(N)]
    print('#{} {}'.format(t,find(0,0)))