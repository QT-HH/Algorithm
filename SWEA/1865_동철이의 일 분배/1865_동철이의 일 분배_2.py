import sys
sys.stdin = open('input.txt')

def dfs(x,s):
    if s * 100 <= result[0]:
        return
    if x >= N:
        result[0] = max(result[0],s*100)
        return
    for i in range(N):
        if not row[i]:
            row[i] = 1
            dfs(x+1 , s*data[x][i]/100)
            row[i] = 0


T = int(input())
for t in range(1,T+1):
    N = int(input())
    data = [list(map(int,input().split())) for _ in range(N)]
    row = [0]*N
    result = [0]
    dfs(0,1)
    res = '%0.6f' % float(result[0])
    print('#{} {}'.format(t,res))
