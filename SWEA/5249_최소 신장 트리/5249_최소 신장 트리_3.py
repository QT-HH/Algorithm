import sys
sys.stdin = open('input.txt')

from heapq import *

def prim(x):
    q = []
    for i in nodes[x]:
        if i not in visited:
            heappush(q,i)



T = int(input())
for t in range(T):
    V,E = map(int,input().split())

    nodes = {}
    visited = [False]*(V+1)
    path = [0]*(V+1)

    for i in range(E):
        a,b,c = map(int,input().split())
        if nodes.get(a):
            nodes[a].append([b,c])
        else:
            nodes[a] = [[b,c]]
        if nodes.get(b):
            nodes[b].append([a,c])
        else:
            nodes[b] = [[a,c]]


