import sys
sys.stdin = open('input.txt')

def cal(idx):
    if tree[idx][1] in opt:
        if tree[idx][1] == '-':
            tree[idx][1] = cal(tree[idx][2])-cal(tree[idx][3])
        elif tree[idx][1] == '+':
            tree[idx][1] = cal(tree[idx][2])+cal(tree[idx][3])
        elif tree[idx][1] == '*':
            tree[idx][1] = cal(tree[idx][2])*cal(tree[idx][3])
        else:
            tree[idx][1] = cal(tree[idx][2])/cal(tree[idx][3])

    return tree[idx][1]

opt = {'-','+','*','/'}
for t in range(1,11):
    N = int(input())
    tree = [[-1]*3 for _ in range(N+1)]
    data = []
    for i in range(1,N+1):
        tmp = input().split()
        if tmp[1] in opt:
            tmp[0],tmp[2],tmp[3] = map(int,(tmp[0],tmp[2],tmp[3]))
        else:
            tmp[0],tmp[1] = map(int, (tmp[0],tmp[1]))
        tree[i] = tmp[:]
    print(f'#{t} {int(cal(1))}')
