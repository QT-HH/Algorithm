import sys
sys.stdin = open('input.txt')

def comb(a,b,c):
    if a == n:
        res.append(tuple(c))
    else:
        for i in range(b,N):
            c[a] = i
            comb(a+1,i+1,c)



N = int(input())
sng = [ list(map(int,input().split())) for _ in range(N) ]

total = 0
for i in range(N):
    total+=sum(i)

cmp = total>>1

n = N//2
tmp = [-1]*n
res = []
comb(0,0,tmp)






