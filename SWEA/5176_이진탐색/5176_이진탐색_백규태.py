import sys
sys.stdin = open('input.txt')

def in_order(idx):
    global cnt
    if idx>N:
        return
    if tree[idx]==-1:
        in_order(idx<<1)
        tree[idx] = cnt
        cnt+=1
        in_order((idx<<1)+1)

test = int(input())
for t in range(1,test+1):
    N = int(input())
    tree = [-1]*(N+1)
    cnt = 1
    in_order(1)
    print(tree)
    print(f'#{t} {tree[1]} {tree[N//2]}')
