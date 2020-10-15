import sys
sys.stdin = open('input.txt')

N,K = map(int,input().split())
t = list(map(int,input().split()))
res = sum(t[:K])
max_t = res
for i in range(K,N):
    res+=t[i]
    res-=t[i-K]
    if res > max_t:
        max_t = res

print(max_t)