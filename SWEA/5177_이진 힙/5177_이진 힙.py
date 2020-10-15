import sys
sys.stdin = open('input.txt')

def heapappend(value):
    global heapcnt
    heapcnt+=1
    tree[heapcnt] = value
    cur = heapcnt
    parent = cur>>1

    while parent and tree[cur] < tree[parent]:
        tree[cur], tree[parent] = tree[parent], tree[cur]
        cur>>=1
        parent>>=1

test = int(input())
for t in range(1,test+1):
    N = int(input())
    data = list(map(int,input().split()))
    heapcnt = 0
    tree = [-1]*(N+1)
    for d in data:
        heapappend(d)
    x = N>>1
    res = 0
    while x:
        res+=tree[x]
        x>>=1
    print(f'#{t} {res}')