def change(x):
    if btree[x+1]==-1:
        if btree[x]>btree[x>>1]:
            btree[x],btree[x>>1] = btree[x>>1], btree[x]
    else:
        while btree[x] > btree[x >> 1] or btree[x >> 1] > btree[x+1]:
            if btree[x] > btree[x >> 1]:
                btree[x], btree[x >> 1] = btree[x >> 1], btree[x]
            if btree[x] > btree[x+1]:
                btree[x], btree[x+1] = btree[x+1], btree[x]


def tappend(x):
    global tcnt
    tcnt+=1
    n = tcnt
    btree[n] = x

    if btree[n>>1]==-1:
        return
    else:
        while n>1:
            if n&1:
                change(n-1)
            else:
                change(n)
            n>>=1

test = int(input())
for t in range(1,test+1):
    N = int(input())
    c = 0
    while (1<<c)<N:
        c+=1
    btree = [-1]*((1<<c)+2)
    tcnt = 0
    for i in range(1,N+1):
        tappend(i)
    print(btree)
    print(btree[1],btree[N//2])