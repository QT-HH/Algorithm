import sys
sys.stdin = open('input.txt')

def btk(idx,cost):

    if cost > result[0]:
        return
    elif idx == N:
        result[0] = min(result[0], cost)


    for i in range(N):
        if not visited[i]:
            visited[i] = 1
            btk(idx+1, cost+costs[idx][i])
            visited[i] = 0


T = int(input())
for t in range(1,T+1):
    N = int(input())
    costs = [list(map(int,input().split())) for _ in range(N)]

    result = [1500]

    visited = [0]*N
    btk(0,0)
    print('#{} {}'.format(t,result[0]))
