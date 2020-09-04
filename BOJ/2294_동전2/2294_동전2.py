import sys
sys.stdin = open('input.txt')

n,k = map(int,input().split())
coin = sorted([int(input()) for _ in range(n)])
a = [0]*100001
dp={}
for i,j in enumerate(a):
    dp[i]=0

total = set()
for c in coin:
    if c > k or c in total:
        continue
    else:
        total.add(c)
        dp[c] = 1
        for i in range(c+1,k+1):
            if dp[i-c]:
                x=dp[i-c]+1
            else:
                continue
            if dp[i]==0 or dp[i]>x:
                dp[i]=x
if dp[k]:
    print(dp[k])
else:
    print(-1)

