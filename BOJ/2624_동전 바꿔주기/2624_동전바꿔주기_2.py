import sys
sys.stdin = open('input.txt')

def exchange(cs,ts,T):
    if T<0 or tuple(set(ts)) in visited:
        return 0
    elif T==0:
        print(ts)
        return 1
    elif sum(ts)==0:
        return 0

    if sum(ts)==0:
        return 0

    for i in range(len(cs)):
        x = ts[:]
        visited.add(tuple(set(x)))
        if x[i]<1:
            continue
        else:
            x[i]-=1
            dp[T] += exchange(cs,x,T-cs[i])
    else:
        return dp[T]

T = int(input())
k = int(input())
visited=set()
coins=[]
cnts=[]
for _ in range(k):
    a,b = map(int,input().split())
    coins.append(a)
    cnts.append(b)
    dp=[0]*(T+1)
print(coins,cnts)
result = exchange(coins,cnts,T)
print(result)
 