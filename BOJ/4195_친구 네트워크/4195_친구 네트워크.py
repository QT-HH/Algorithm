import sys
sys.stdin = open('input.txt')

def getParent(parents,x):
    if parents[x] == x:
        return x
    p = getParent(parents, parents[x])
    parents[x] = p
    return p

def unionParent(parents,x1,x2,cnt):
    a = getParent(parents, x1)
    b = getParent(parents, x2)
    if a!=b:
        parents[b] = a
        cnt[a] += cnt[b]

T = int(input())
for t in range(1,T+1):
    n = int(sys.stdin.readline())
    friends = {}
    cnt = {}
    for i in range(n):
        a,b = sys.stdin.readline().split()
        if a not in friends:
            friends[a] = a
            cnt[a] = 1
        if b not in friends:
            friends[b] = b
            cnt[b] = 1
        unionParent(friends,a,b,cnt)
        print(cnt[getParent(friends,a)])


