import sys
sys.stdin = open('input.txt')

N = int(input())
li = list(map(int,input().split()))
max_li = 1
cnt_up = 1
cnt_dn = 1
for i in range(1,N):
    if li[i] >= li[i-1]:
        cnt_up+=1
    else:
        cnt_up=1

    if li[i] <= li[i-1]:
        cnt_dn+=1
    else:
        cnt_dn=1

    if max_li < cnt_up:
        max_li = cnt_up
    if max_li < cnt_dn:
        max_li = cnt_dn

print(max_li)
