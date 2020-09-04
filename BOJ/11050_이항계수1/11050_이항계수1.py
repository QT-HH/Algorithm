N,K = map(int,input().split())
dp=[[1] for _ in range(12)]
dp[2] = [1,1]
for i in range(2,N+1):
    for j in range(1,len(dp[i])):
        dp[i+1].append(dp[i][j-1]+dp[i][j])
    dp[i+1].append(1)

print(dp[N+1][K])
