import sys
sys.stdin = open('input.txt')

def getParent(x):
    if parent[x] == x:
        return x
    else:
        parent[x] = getParent(parent[x])
        return parent[x]

def union(x,y):
    a = getParent(x)
    b = getParent(y)

    if a != b:
        parent[b] = a

T = int(input())

for t in range(1,T+1):
    V,E = map(int,input().split())
    nodes = sorted([[*map(int,input().split())] for _ in range(E)],key=lambda x:x[2])

    parent = list(range(V+1))
    total = 0
    for i in nodes:
        if getParent(i[0]) == getParent(i[1]):
            continue
        else:
            union(i[0],i[1])
            total += i[2]

    print('#{} {}'.format(t,total))