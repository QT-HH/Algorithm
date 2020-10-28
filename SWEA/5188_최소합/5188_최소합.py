import sys
sys.stdin = open('input.txt')


def comb(a,b,c):
    # a = 현재 인덱스
    # b = board 인덱스
    # c = 길이
    if a == c:
        tmp_val = board[0][0]
        for j in range((N - 1) * 2):
            if j in tmp:
                direct[j] = 1
            else:
                direct[j] = 0

        y = 0
        x = 0
        for j in direct:
            if j:
                y += 1
            else:
                x += 1
            tmp_val += board[x][y]

        if min_val[0] > tmp_val:
            min_val[0] = tmp_val
        return
    else:
        for i in range(b,c*2):
            tmp[a] = i
            comb(a+1,i+1,c)


T = int(input())
for t in range(1,T+1):
    N = int(input())
    board = [list(map(int,input().split())) for _ in range(N)]
    result = []
    tmp = [0]*(N-1)
    direct = [0] * (N - 1) * 2
    min_val = [2000]
    comb(0,0,N-1)

    print('#{} {}'.format(t,min_val[0]))
