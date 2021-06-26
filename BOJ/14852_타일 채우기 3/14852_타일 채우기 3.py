import sys
sys.stdin = open('input.txt')
input = sys.stdin.readline

N = int(input().rstrip())
m = 1000000007
res = [0]*(N+10)
res2 = [0]*(N+10)
res[0] = 1
res[1] = 2
res[2] = 7
res[3] = 22
res2[3] = 1
for i in range(4,N+1):
    res2[i] = (res2[i-1]+res[i-3]) % m
    res[i] = (res[i-1]*2 + res[i-2]*3 + res2[i]*2) % m

print(res[N] % m)
