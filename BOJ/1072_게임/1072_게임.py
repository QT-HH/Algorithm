import sys
sys.stdin = open('input.txt')

X,Y = map(int,input().split())
Z = int(Y*100 / X)
l,r = 0,1000000000
while r-l > 1:
    c = (l+r)//2
    if int((Y+c) * 100 / (X+c)) <= Z:
        l = c
    else:
        r = c

right = int((Y+r) * 100 / (X+r))
left = int((Y+l) * 100 / (X+l))

if right > left:
    print(r)
elif right == left and left == Z:
    print(-1)
else:
    print(l)
