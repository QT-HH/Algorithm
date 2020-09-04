import sys
sys.stdin = open('input.txt')

T = int(input())
for i in range(T):
    N = int(input())
    coin = list(map(int,input().split()))
    M = int(input())
    dp = [0]*(M+1)

    for c in coin:
        if c>M:
            continue
        else:
            dp[c]+=1
        for i in range(c,M+1):
            if i-c>=0:
                dp[i]+=dp[i-c]
            else:
                continue
    print(dp[M])