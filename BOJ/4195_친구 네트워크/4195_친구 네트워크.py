import sys
sys.stdin = open('input.txt')

T = int(input())
for t in range(1,T+1):
    n = int(input())

    for i in range(n):
        a,b = input().split()
        print(a,b)