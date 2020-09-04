import sys
sys.stdin = open('input.txt')

def fac(n):
    res = 1
    for i in range(1,n+1):
        res*=i
    return res

test = int(input())
for t in range(1,1+test):
    N = int(input())
    result = 0
    if N//10%2:
        for i in range(1,N//10+1,2):
            a = (N//10-i)//2
            b = a+i
            result += fac(b)//(fac(a)*fac(i)) * 2 ** a
    else:
        for i in range(0,N//10+1,2):
            a = (N//10-i)//2
            b = a+i
            result += fac(b) // (fac(a) * fac(i)) * 2 ** a

    print(f'#{t} {result}')