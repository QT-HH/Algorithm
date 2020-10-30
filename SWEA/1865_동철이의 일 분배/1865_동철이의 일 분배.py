import sys
sys.stdin = open('input.txt')

def adj(x):
    for i in range(x):
        if row[x] == row[i]:
            return False
    return True

def dfs(x):
    if x == N:
        tmp = 1
        for i in range(N):
            tmp *= (data[i][row[i]]*0.01)
        tmp = tmp*100

        if result[0] <= tmp:
            result[0] = tmp

    else:
        for i in range(N):
            row[x] = i
            if adj(x):
                dfs(x+1)

T = int(input())
for t in range(1,T+1):
    N = int(input())
    data = [list(map(int,input().split())) for _ in range(N)]
    row = [0]*N
    result = [0]
    dfs(0)
    res = '%0.6f' % float(result[0])
    print('#{} {}'.format(t,res))
