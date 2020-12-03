import sys
sys.stdin = open('input.txt')

T = int(input())
for t in range(1,T+1):
    prices = list(map(int,input().split()))
    plan = list(map(int,input().split()))
    now = [0]*12
    for i in range(12):
        if plan[i]:
            now[i] = min(prices[0]*plan[i],prices[1])

    for i in range(12):
        if now[i]:
            if prices[2] < sum(now[i:i+3]):
                now[i] = prices[2]
                if i < 10:
                    now[i+1] = 0
                    now[i+2] = 0
                elif i < 11:
                    now[i+1] = 0

    result = min(prices[3], sum(now))
    print('#{} {}'.format(t,result))
