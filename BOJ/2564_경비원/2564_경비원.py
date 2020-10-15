import sys
sys.stdin = open('input.txt')

def find(dg,c):
    for i in stores:
        if i[0] == c:
            if i[0] in (1,2):
                if i[2]+dg[2] <= X:
                    total[0] += (i[2]+dg[2]+Y)
                else:
                    total[0] += (2*X-i[2]-dg[2]+Y)
            else:
                if i[1]+dg[1] <= Y:
                    total[0] += (i[1]+dg[1]+X)
                else:
                    total[0] += (2*Y-i[1]-dg[1]+X)
                print(total,2)
        else:
            total[0] += (abs(dg[1]-i[1]) + abs(dg[2]-i[2]))

X,Y = map(int,input().split())
N = int(input())
stores = []
for _ in range(N+1):
    a,b = map(int,input().split())
    if a==1:
        stores.append((a,0,b))
    elif a==2:
        stores.append((a,Y,b))
    elif a==3:
        stores.append((a,b,0))
    elif a==4:
        stores.append((a,b,X))

dg = stores.pop()
total = [0]
if dg[0] == 1:
    find(dg,2)
elif dg[0] == 2:
    find(dg,1)
elif dg[0] == 3:
    find(dg,4)
elif dg[0] == 4:
    find(dg,3)

print(total[0])