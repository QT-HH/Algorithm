import sys
sys.stdin = open('input.txt')

data = [list(map(int,input().split())) for _ in range(4)]
fir = []
sec = []
for i in data:
    fir.append(i[:4])
    sec.append(i[4:])

for i in range(4):
    x1,y1,x2,y2 = fir[i]
    p1,q1,p2,q2 = sec[i]

    if x2<p1 or p2<x1 or y2<q1 or q2<y1:
        print('d')
    elif x2==p1 or x1==p2:
        if y2==q1 or y1==q2:
            print('c')
        else:
            print('b')
    elif y2==q1 or y1==q2:
        if x2==p1 or x1==p2:
            print('c')
        else:
            print('b')
    else:
        print('a')