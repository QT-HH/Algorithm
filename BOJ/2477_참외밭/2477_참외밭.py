import sys
sys.stdin = open('input.txt')

now = [(0,0)]
K = int(input())
for _ in range(6):
    d,l = map(int,input().split())
    if d==1:
        now.append((now[-1][0] + l, now[-1][1]))
    elif d==2:
        now.append((now[-1][0] - l, now[-1][1]))
    elif d==3:
        now.append((now[-1][0], now[-1][1] - l))
    elif d==4:
        now.append((now[-1][0], now[-1][1] + l))

max_x = -1000
min_x = 1000
max_y = -1000
min_y = 1000
for n in now:
    if max_x < n[0]:
        max_x = n[0]
    elif min_x > n[0]:
        min_x = n[0]

    if max_y < n[1]:
        max_y = n[1]
    elif min_y > n[1]:
        min_y = n[1]

big = (max_x-min_x)*(max_y-min_y)

for n in now:
    if min_x < n[0] < max_x and min_y < n[1] < max_y:
        center = n

for i in [(max_x,max_y),(max_x,min_y),(min_x,max_y),(min_x,min_y)]:
    if i not in now:
        small = abs((i[0]-center[0])*(i[1]-center[1]))
        break

print((big-small)*K)