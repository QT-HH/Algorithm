import sys
sys.stdin = open('input.txt')

def srt(x):
    if x == []:
        return []
    pivot = x[0][0]
    left = []
    right = []
    center = []
    for i in x:
        if i[0] > pivot:
            left.append(i)
        elif i[0] < pivot:
            right.append(i)
        else:
            center.append(i)
    return srt(left)+center+srt(right)

T = int(input())
k = int(input())
coins_n = [list(map(int,input().split())) for _ in range(k)]
coins = srt(coins_n)
dp=[0]*(T+1)
total = [0]

for coin in coins:
    temp=[]
    if coin[0] > T or coin[1] < 1:
        continue

    for spot in total:
        for i in range(spot+coin[0],spot+coin[0]*coin[1]+1,coin[0]):
            if i<coin[0] or i > T:
                continue
            else:
                dp[i]+=1
                temp.append(i)
    total.extend(temp)

print(dp[T])