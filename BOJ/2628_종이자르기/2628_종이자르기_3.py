import sys
sys.stdin = open('input.txt')

w,h = map(int,input().split())
n = int(input())

cut_x = [0,h]
cut_y = [0,w]
for _ in range(n):
    a,b = map(int,input().split())
    if a:
        cut_y.append(b)
    else:
        cut_x.append(b)

cut_x.sort()
cut_y.sort()

max_w = 0
max_h = 0
for i in range(1,len(cut_x)):
    cut = cut_x[i]-cut_x[i-1]
    if max_h < cut:
        max_h = cut
for i in range(1,len(cut_y)):
    cut = cut_y[i]-cut_y[i-1]
    if max_w < cut:
        max_w = cut

print(max_h*max_w)