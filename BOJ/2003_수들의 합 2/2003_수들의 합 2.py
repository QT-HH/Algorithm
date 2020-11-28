import sys
sys.stdin = open('input.txt')

N,M = map(int,input().split())
li = list(map(int,input().split()))

tmp = {}
tmp[li[0]] = 1
for i in range(1,N):
    li[i] += li[i-1]
    tmp[li[i]] = 1

cnt = 0
for i in range(N):
    if li[i] == M:
        cnt+=1
    elif li[i] > M and tmp.get(li[i]-M):
        cnt+=1

print(cnt)