import sys
sys.stdin = open('input.txt')
import heapq
input = sys.stdin.readline
INF =  float('inf')

def getParent(parents, x):
    if parents[x] == x:
        return x
    p = getParent(parents, parents[x])
    parents[x] = p
    return p

def unionParent(parents, x1, x2):
    a = getParent(parents, x1)
    b = getParent(parents, x2)
    if a != b:
        parents[b] = a

N,M = map(int,input().rstrip().split())
nodes = []
for _ in range(M+1):
    A,B,C = map(int,input().rstrip().split())
    if C:
        C-=1
    else:
        C+=1

    nodes.append((C,A,B))

nodes.sort(key=lambda x:x[0])
parent = list(range(N+1))
total_min = 0
for i in nodes:
    if getParent(parent, i[1]) != getParent(parent, i[2]):
        unionParent(parent, i[1], i[2])
        total_min += i[0]

parent = list(range(N+1))
total_max = 0
for j in nodes[::-1]:
    if getParent(parent, j[1]) != getParent(parent, j[2]):
        unionParent(parent, j[1], j[2])
        total_max += j[0]

print(total_max*total_max - total_min*total_min)


