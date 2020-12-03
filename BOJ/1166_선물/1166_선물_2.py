import sys
sys.stdin = open('input.txt')

N,L,W,H = map(int,input().split())

small = min(L,W,H)
x = L // small
y = W // small
z = H // small

while x*y*z < N:
    a = L / (x+1)
    b = W / (y+1)
    c = H / (z+1)
    small = max(a,b,c)

    if small == a:
        x += 1
    elif small == b:
        y += 1
    else:
        z += 1

print(small)