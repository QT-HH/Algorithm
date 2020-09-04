import sys
sys.stdin = open('input.txt')

def ladder(before):

    if before == (1<<N)-1:
        return
    # elif dp[before]>=B:
    #     return

    for i in range(N):
        if (before>>i) % 2 == 0:
            x = before|(1<<i)
            if dp[x]:
                continue
            dp[x] = dp[before]+H[i]
            if dp[x] >= B and dp[x] <= result[0]:
                result[0] = dp[x]
                continue
            ladder(x)
    return


test = int(input())
for t in range(1,test+1):
    N, B = map(int, input().split())
    H = list(map(int, input().split()))
    dp = [0]*(1<<N)
    result = [10000*20+1]
    ladder(0)
    print(f'#{t} {result[0]-B}')