T = int(input())

for j in range(0, T):
    x = list(map(int,input().split()))
    while len(x)!=1:
        if x[0]>x[1]:
            x.pop(1)
        elif x[0]<x[1]:
            x.pop(0)
        elif x[0]==x[1]:
            x.pop(0)
    print(x[0])