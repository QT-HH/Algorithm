import sys
n = list(map(int,sys.stdin.read().split()))

def fac(n):
    res = 1
    for i in range(1,n+1):
        res*=i
    return res

for N in n:
    N = int(input())
    result = 0
    if N%2:
        for i in range(1,N+1,2):
            a = (N-i)//2
            b = a+i
            result += fac(b)//(fac(a)*fac(i)) * 2 ** a
    else:
        for i in range(0,N+1,2):
            a = (N-i)//2
            b = a+i
            result += fac(b) // (fac(a) * fac(i)) * 2 ** a

    print(result)