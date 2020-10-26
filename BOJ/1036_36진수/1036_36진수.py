import sys
sys.stdin = open('input.txt')

N = int(input())
nums = [ list(input()) for _ in range(N)]
K = int(input())

dex = {}
alp = ['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']
for i in range(10):
    dex[str(i)] = i
for i in range(len(alp)):
    dex[alp[i]] = i+10


