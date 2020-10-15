import sys
sys.stdin = open('input.txt')

N = int(input())
lotto = list(map(int,input().split()))
std = [i for i in range(1,N+1)]
cnt = 0
for i in lotto:
    for j in range(cnt,cnt-i,-1):
        std[j], std[j-1] = std[j-1], std[j]
    cnt+=1

print(*std)