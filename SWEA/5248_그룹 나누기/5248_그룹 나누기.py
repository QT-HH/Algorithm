import sys
sys.stdin = open('input.txt')

def getParents(x):
    if friends[x] == x:
        return x
    else:
        friends[x] = getParents(friends[x])
        return friends[x]

def union(x,y):
    a = getParents(x)
    b = getParents(y)

    if a != b:
        friends[b] = a


T = int(input())
for t in range(1,T+1):
    N,M = map(int,input().split())
    pairs = list(map(int,input().split()))
    friends = {n:n for n in range(1,N+1)}

    for i in range(0,len(pairs),2):
        union(pairs[i],pairs[i+1])

    group = set()
    cnt = 0
    for i in friends:
        if getParents(i) not in group:
            group.add(friends[i])
            cnt+=1

    print('#{} {}'.format(t,cnt))
