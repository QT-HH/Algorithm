import sys
sys.stdin = open('input.txt')

def btk(idx,oil,cnt):
    # oil : 남은 연료
    # idx : 현재 인덱스
    # cnt : 바꾼 횟수
    if oil < 0:
        return
    elif idx == N:
        result[0] = min(result[0],cnt)
        return
    elif result[0] <= cnt:
        return
    else:
        btk(idx + 1, oil - 1, cnt)
        btk(idx + 1, bat[idx] - 1, cnt + 1)


T = int(input())
for t in range(1,T+1):
    bat = list(map(int,input().split()))
    N = bat[0]
    result = [N]

    btk(1, bat[1], 0)

    print('#{} {}'.format(t,result[0]))
