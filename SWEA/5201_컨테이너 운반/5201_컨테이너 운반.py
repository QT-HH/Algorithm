import sys
sys.stdin = open('input.txt')

T = int(input())
for t in range(1,T+1):
    N,M = map(int,input().split())
    Ws = sorted(list(map(int,input().split())),reverse=True)
    Ts = list(map(int,input().split()))

    result = 0

    for i in Ws:
        for j in Ts:
            if i <= j:
                result += i
                Ts.remove(j)
                break

    print('#{} {}'.format(t,result))