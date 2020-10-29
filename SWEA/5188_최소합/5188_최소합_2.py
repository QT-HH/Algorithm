import sys,itertools
sys.stdin = open('input.txt')

def comb(a,b,c,d):
    # a = 현재 인덱스
    # b = y 남은 횟수
    # c = x 남은 횟수
    # d = 마지막 인덱스

    if c:
        tmp[a] = 1
        comb(a+1,b,c-1,d)
    if b:
        tmp[a] = 0
        comb(a+1,b-1,c,d)

    if a == d:
        y = 0
        x = 0
        tmp_val = board[0][0]
        for t in tmp:
            if t:
                y+=1
            else:
                x+=1
            tmp_val += board[y][x]
            if tmp_val >= result[0]:
                break

        if tmp_val < result[0]:
            result[0] = tmp_val
    return

T = int(input())
for t in range(1,T+1):
    N = int(input())
    board = [list(map(int,input().split())) for _ in range(N)]
    result = [2000]
    remain = (N-1)
    tmp = [0]*remain*2
    comb(0,remain,remain,remain*2-1)

    print('#{} {}'.format(t,result[0]))
