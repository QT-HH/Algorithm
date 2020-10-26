N = 4

def isPrime(N):
    for i in range(2,N//2+1):
        if not N%i:
            return i
    return 1

print(isPrime(N))