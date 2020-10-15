import sys
sys.stdin = open('inpurt.txt')

def tree_sum(idx):
    if idx>N:
        return 0
    elif tree[idx] == -1:
        tree[idx] = tree_sum(idx<<1) + tree_sum((idx<<1)+1)
    return tree[idx]

test = int(input())
for t in range(1,test+1):
    N,M,L = map(int,input().split())
    data = [tuple(map(int,input().split())) for _ in range(M)]
    tree = [-1]*(N+1)
    for d in data:
        tree[d[0]] = d[1]
    print(f'#{t} {tree_sum(L)}')

