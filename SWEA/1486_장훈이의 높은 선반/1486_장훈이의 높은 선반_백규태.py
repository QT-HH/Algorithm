import sys
sys.stdin = open('input.txt')

def ladder(x,m):
    if m >= B and m <= result[0]:
        result[0] = m
    elif x == N:
        return
    else:
        dp[x] = 0
        ladder(x+1,m)
        dp[x] = 1
        ladder(x+1,m+H[x])

test = int(input())
for t in range(1,test+1):
    N,B = map(int,input().split())
    H = list(map(int,input().split()))
    dp = [0]*N
    result = [200000000]
    ladder(0,0)
    print(f'#{t} {result[0]-B}')