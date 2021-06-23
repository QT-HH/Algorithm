import sys
sys.stdin = open('input.txt')
input = sys.stdin.readline

def getParent(parent, x):
    if parent[x] == x:
        return x
    else:
        p = getParent(parent, parent[x])
        parent[x] = p
        return p

def union(parent, x, y):
    xp = getParent(parent, x)
    yp = getParent(parent, y)
    if xp != yp:
        parent[yp] = xp

V,E = map(int,input().rstrip().split())
nodes = []
for _ in range(E):
    A,B,C = map(int,input().rstrip().split())
    A -= 1
    B -= 1
    nodes.append((C,A,B))

nodes.sort(key=lambda x:x[0])
parents = [*range(V)]
total = 0
for i in nodes:
    x = getParent(parents, i[1])
    y = getParent(parents, i[2])
    if x != y:
        total += i[0]
        union(parents, i[1], i[2])

print(total)