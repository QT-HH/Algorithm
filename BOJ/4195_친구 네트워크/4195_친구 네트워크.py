import sys
sys.stdin = open('input.txt')

def getParent(parents,x):
    if parents[x] == x:
        return x
    p = getParent(parents, parents[x])
    parents[x] = p
    return p

T = int(input())
for t in range(1,T+1):
    n = int(input())
    friends = {}
    for i in range(n):
        a,b = input().split()
