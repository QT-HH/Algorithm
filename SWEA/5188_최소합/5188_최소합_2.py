import sys
sys.stdin = open('input.txt')

T = int(input())
for t in range(1,T+1):
    N = int(input())
    board = [list(map(int,input().split())) for _ in range(N)]

    stack = [[0]*(N-1)*2]
    direct = [(0,1),(1,0)]
    while stack:
