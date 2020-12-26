import sys
sys.stdin = open('input.txt')

N,S = map(int,input().split())
li = list(map(int,input().split()))

res = N+1
tail = 0
tmp = li[0]
for i in range(1,N):
    tmp += li[i]
    if tmp >= S:
        while tmp >= S:
            tmp -= li[tail]
            tail += 1
        else:
            res = min(res,i-tail+2)

if res > N:
    print(0)
else:
    print(res)