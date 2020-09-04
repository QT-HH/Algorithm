import sys
sys.stdin = open('input.txt')

n,k = map(int,input().split())
coin = [int(i) for i in range(n)]

dp = [0]+[99999]*k
for i in range(min(coin),k+1):
    dp[i] = min(dp[i-x] for x in coin if i-x>=0) + 1
print(-1) if dp[k] > k else print(dp[k])