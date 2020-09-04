def fib(n):
    if n <=0:
        return 0
    elif n==1:
        return 1
    elif n==2:
        return 1
    elif n in fb:
        return fb[n]
    elif n%2:
        x = fib(n//2)
        y = fib(n//2+1)

        fb[n] = x*x + y*y
        return fb[n]
    else:
        x = fib(n//2-1)
        y = fib(n//2)
        fb[n] = y*(y+2*x)
        return fb[n]

fb = {}
N = int(input())
print(fib(N)%1000000007)
