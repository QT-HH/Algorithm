import sys
sys.stdin = open('sample_input.txt')
n,k = map(int,input().split())
coin = [int(input()) for _ in range(n)]
dp = [0]*(k+1)

for c in coin:
    dp[c] +=1
    for i in range(c,k+1):
        dp[i]+=dp[i-c]

print(dp[k])