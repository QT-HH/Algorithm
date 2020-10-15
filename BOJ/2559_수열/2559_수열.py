import sys
sys.stdin = open('input.txt')

N,K = map(int,input().split())
t = list(map(int,input().split()))
max_t = -999999999
for i in range(1,N):
    t[i] += t[i-1]
t.append(0)
for i in range(N-1,K-2,-1):
    t[i] -= t[i-K]
    if t[i] > max_t:
        max_t = t[i]

print(max_t)