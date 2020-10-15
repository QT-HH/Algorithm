import sys
sys.stdin = open('input.txt')

import collections
test = int(input())
for t in range(1,test+1):
    V,E,x,y = map(int,input().split())
    data = list(map(int,input().split()))
    tree1 = []
    tree2 = []