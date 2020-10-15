import sys
sys.stdin = open('input.txt')

w,h = map(int,input().split())
x,y = map(int,input().split())
t = int(input())

x+=t
y+=t

nx,mx = x//w, x%w
ny,my = y//h, y%h

result = [0,0]
if nx&1 or ny&1:
    if nx&1 and ny&1:
        result[0] = w-mx
        result[1] = h-my
    elif nx&1:
        result[0] = w-mx
        result[1] = my
    else:
        result[0] = mx
        result[1] = h-my
else:
    result[0] = mx
    result[1] = my

print(*result)
