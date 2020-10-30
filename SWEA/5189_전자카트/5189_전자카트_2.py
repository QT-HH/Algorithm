import sys
sys.stdin = open('input.txt')

def find():
    pass

T = int(input())
for t in range(1,T+1):
    N = int(input())
    path = [list(map(int,input().split())) for _ in range(N)]
    