import sys
sys.stdin = open('input.txt')

N = int(input())
li = list(map(int,input().split()))
max_li = 0
cnt = 1
for i in range(1,N):
    if li[i] >= li[i-1]:
        cnt+=1
    else:
        cnt=1
    if max_li < cnt:
        max_li = cnt

cnt = 1
for i in range(1, N):
    if li[i] <= li[i-1]:
        cnt+=1
    else:
        cnt=1
    if max_li < cnt:
        max_li = cnt

if N==1:
    print(1)
else:
    print(max_li)
