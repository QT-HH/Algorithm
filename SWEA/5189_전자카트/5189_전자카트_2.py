import sys
sys.stdin = open('input.txt')

def find(idx,tmp):
    if result[0] < tmp:
        return
    elif idx == N:
        result[0] = min(result[0],tmp)
    else:
        for i in range(idx,N):
            # if i != idx:
            odr[i], odr[idx] = odr[idx], odr[i]
            find(idx+1,tmp+path[idx][odr[i]])
            odr[i], odr[idx] = odr[idx], odr[i]

T = int(input())
for t in range(1,T+1):
    N = int(input())
    path = [list(map(int,input().split())) for _ in range(N)]
    odr = list(range(N))
    result = [10000]
    find(1,0)
    print(result[0])