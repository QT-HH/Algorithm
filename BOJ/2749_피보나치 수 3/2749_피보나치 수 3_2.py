def mul(x,y):
    a = (x[0]*y[0] + x[1]*y[2]) %1000000
    b = (x[0]*y[1] + x[1]*y[3]) %1000000
    c = (x[2]*y[0] + x[3]*y[2]) %1000000
    d = (x[2]*y[1] + x[3]*y[3]) %1000000
    return a,b,c,d

def fib(n):
    a = [1,0,0,1]
    b = [1,1,1,0]
    while n > 0:
        if n & 1:
            a = mul(a,b)
        b = mul(b,b)
        n >>= 1
    return a[1]
n = int(input())
print(fib(n))