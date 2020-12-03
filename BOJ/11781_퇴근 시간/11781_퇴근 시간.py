import sys
sys.stdin = open('input.txt')

N,M,S,E = map(int,input().split())
A,B,L,t1,t2 = map(int,input().split())

visited = [0]*(N+1)


