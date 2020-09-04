import sys
sys.stdin = open('sample_input.txt')

def comb(v,s,res):
    if v == 2:
        result.append(tuple(res))
    else:
        for i in range(s,N-1):
            res[v] = i
            comb(v+1,i+1,res)

T = int(input())
for test_case in range(1, T + 1):
    N, M = map(int, input().split())
    board = [input() for _ in range(N)]
    result = []
    res = [0] * 2
    comb(0, 0, res)

    new_board = []
    for i in range(N):
        w = board[i].count('W')
        b = board[i].count('B')
        new_board.append([w, b, M - (w + b)])
    for i in range(1, N):
        new_board[i][0] += new_board[i - 1][0]
        new_board[i][1] += new_board[i - 1][1]
        new_board[i][2] += new_board[i - 1][2]

    rex = 0
    for i in result:
        white = new_board[i[0]][0]
        blue = new_board[i[1]][1] - new_board[i[0]][1]
        red = new_board[N - 1][2] - new_board[i[1]][2]
        total = white + blue + red
        if rex < total:
            rex = total

    print(f'#{test_case} {N * M - rex}')

