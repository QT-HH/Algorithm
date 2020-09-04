import sys
sys.stdin = open('input.txt')

test = int(input())
for t in range(1,1+test):
    N = int(input())
    dp = [0]*(N//10+1)
    dp[0], dp[1] = 1, 1
    for i in range(2,N//10+1):
        dp[i] = dp[i-1]+2*dp[i-2]

    print(f'#{t} {dp[N//10]}')