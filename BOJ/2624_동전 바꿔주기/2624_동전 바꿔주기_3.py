import sys
sys.stdin = open('input.txt')

T = int(input())
k = int(input())
dic = {}
for _ in range(k):
    x,y = map(int,input().split())
    dic[x] = y


