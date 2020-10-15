import sys
sys.stdin = open('input.txt')

N,M = map(int,sys.stdin.readline().split())
x = list(map(int,sys.stdin.readline().split()))
for i in range(len(x)-1):
    x[i+1]+=x[i]
x.append(0)
for _ in range(M):
    a,b = map(int,sys.stdin.readline().split())
    print(x[b-1]-x[a-2])