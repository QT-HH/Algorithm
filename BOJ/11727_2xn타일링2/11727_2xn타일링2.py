N = int(input())
dp=[1]*(N+1)
for i in range(2,N+1):
    dp[i] = dp[i-1]+2*dp[i-2]
print(dp[N]%10007)