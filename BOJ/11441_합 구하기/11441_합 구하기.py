import sys
sys.stdin = open('input.txt')

N = int(sys.stdin.readline())
A = list(map(int,sys.stdin.readline().split()))
for i in range(N-1):
    A[i+1] += A[i]
A.append(0)
M = int(sys.stdin.readline())
for _ in range(M):
    i,j = map(int,sys.stdin.readline().split())
    print(A[j-1]-A[i-2])