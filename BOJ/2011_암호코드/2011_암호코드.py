import sys
sys.stdin = open('input.txt')

def find():
    if len(num) >=1:
        if num[0] == 0:
            return 0
        else:
            dp[0] = 1
    if len(num) >=2:
        if num[0] == 0:
            return 0
        elif num[1] == 0:
            if num[0]*10 + num[1] <= 26:
                dp[1] = 1
        else:
            if num[0]*10 + num[1] <= 26:
                dp[1] = 2
            else:
                dp[1] = 1

    for i in range(2,len(num)):
        if num[i-1] == 0:
            if num[i] == 0:
                return 0
            dp[i] += dp[i-1]
        elif num[i] == 0:
            if num[i-1]*10 + num[i] <= 26:
                dp[i] += dp[i-2]
        else:
            if num[i-1]*10 + num[i] <= 26:
                dp[i] += dp[i-2]+dp[i-1]
            else:
                dp[i] += dp[i-1]

    return dp[-1]%1000000

num = [*map(int,input())]
dp = [0]*len(num)
if len(num) == 0:
    print(0)
else:
    print(find())
    print(dp)