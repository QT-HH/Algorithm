import sys
sys.stdin = open('input.txt')

T = int(input())
for t in range(1,T+1):
    N = int(input())
    board = [[*map(int,input().split())] for _ in range(N)]
    go = [[0]*N for _ in range(N)]

    for i in range(1,N):
        if board[0][i] > board[0][i-1]:
            go[0][i] = go[0][i-1] + 1 + board[0][i]-board[0][i-1]
        else:
            go[0][i] = go[0][i-1] + 1

        if board[i][0] > board[i-1][0]:
            go[i][0] = go[i-1][0] + 1 + board[i][0] - board[i-1][0]
        else:
            go[i][0] = go[i-1][0] + 1

    for i in range(1,N):
        for j in range(1,N):
            if board[i][j] > board[i][j-1]:
                tmp1 = go[i][j-1] + 1 + board[i][j] - board[i][j-1]
            else:
                tmp1 = go[i][j - 1] + 1

            if board[j][i] > board[j][i - 1]:
                tmp2 = go[j][i - 1] + 1 + board[j][i] - board[j][i - 1]
            else:
                tmp2 = go[j][i - 1] + 1

            go[i][j] = min(tmp1,tmp2)

    print('#{} {}'.format(t,go[N-1][N-1]))
