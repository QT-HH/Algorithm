import sys
sys.stdin = open('input.txt')

N,M = map(int,sys.stdin.readline().split())
x = [[0]*(N+1) for _ in range(N+1)]
for _ in range(M):
    A,B = map(int,sys.stdin.readline().split())
    x[A][B] = 1






