import sys
sys.stdin = open('input.txt')

N,M = map(int,input().split())
li = list(map(int,input().split()))

tmp = {li[0]:1}
cnt = 0
if li[0] == M:
    cnt+=1

for i in range(1,N):
    li[i] += li[i-1]

    if li[i] == M:
        cnt+=1
        if tmp.get(0):
            cnt+=tmp[0]
    elif tmp.get(li[i]-M):
        cnt+=tmp[li[i]-M]

    if tmp.get(li[i]):
        tmp[li[i]] += 1
    else:
        tmp[li[i]] = 1

print(cnt)
