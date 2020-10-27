import sys
sys.stdin = open('input.txt')

hex = {'0': '0000', '1': '0001', '2': '0010', '3': '0011', '4': '0100', '5': '0101',
       '6': '0110', '7': '0111', '8': '1000', '9': '1001',
       'A': '1010', 'B': '1011', 'C': '1100', 'D': '1101', 'E': '1110', 'F': '1111'}
code_pattern = {'112': 0, '122': 1, '221': 2, '114': 3, '231': 4, '132': 5, '411': 6, '213': 7, '312': 8, '211': 9}

T = int(input())
for tc in range(1, T + 1):
    N, M = map(int, input().split())  # N세로 M가로
    board = [list(input()) for _ in range(N)]
    # for i in board:
    #     print(i)

    # 16진수 -> 2진수
    bi_li = [''] * N
    for i in range(N):
        for j in range(M):
            bi_li[i] += hex[board[i][j]]
    for i in bi_li:
        print(i)