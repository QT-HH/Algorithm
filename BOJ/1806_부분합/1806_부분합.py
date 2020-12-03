import sys
sys.stdin = open('input.txt')

N,S = map(int,input().split())
li = list(map(int,input().split()))

if li[0] >= S:
    print('1')
else:
    for i in range(1,N):
        li[i] += li[i-1]
        while li[i] >= S:

