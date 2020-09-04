import sys
sys.stdin = open('sample_input.txt')

T = int(input())
for test_case in range(1, T + 1):
    N, M = map(int, input().split())
    board = [input() for _ in range(N)]

    new_board = []
    for i in range(N):
        w = board[i].count('W')
        b = board[i].count('B')
        new_board.append([w, b, M - (w + b)])
    for i in range(1, N):
        new_board[i][0] += new_board[i - 1][0]
        new_board[i][1] += new_board[i - 1][1]
        new_board[i][2] += new_board[i - 1][2]

    res = 0
    for x in range(N - 2):
        for y in range(x + 1, N - 1):
            white = new_board[x][0]
            blue = new_board[y][1] - new_board[x][1]
            red = new_board[N - 1][2] - new_board[y][2]
            total = white + blue + red
            if res < total:
                res = total
    print(f'#{test_case} {N * M - res}')

