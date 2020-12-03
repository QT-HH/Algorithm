import sys
sys.stdin = open('input.txt')

N = int(input())
col = []
point = []
max_H = 0
min_L = 1001
max_L = 0
for i in range(N):
    L, H = map(int, input().split())
    col.append([L,H])
    if max_H < H:
        max_H = H
    if min_L > L:
        min_L = L
    if max_L < L:
        max_L = L

size = (max_L+1-min_L)*max_H
col.sort(key= lambda x : x[0])
for i in range(len(col)):
    if col[i][1]==max_H:
        center = i
        break

left = sorted(col[:center], key=lambda x: -x[1])
right = sorted(col[center+1:], key=lambda x: -x[1])

print(left)

h = col[center][1]
min_l = col[center][0]
for i in left:
    if min_l > i[0]:
        a = min_l-i[0]
        b = col[center][1]-i[1]
        min_l = i[0]
        size-=a*b

h = col[center][1]
max_l = col[center][0]
for i in right:
    if max_l < i[0]:
        a = i[0]+1-(max_l+1)
        b = col[center][1]-i[1]
        max_l = i[0]
        size-=a*b

print(size)