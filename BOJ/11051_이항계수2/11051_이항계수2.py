import sys
sys.stdin = open('input.txt')

N,K = map(int,input().split())
dp = [[1] for _ in range(N+1)]
dp[0]=[1]
dp[1]=[1,1]
for i in range(1,N):
    for j in range(len(dp[i])-1):
        dp[i+1].append(dp[i][j]+dp[i][j+1])
    dp[i+1].append(1)

print(dp)
print(dp[N][K]%10007)