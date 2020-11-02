import sys
sys.stdin = open('input.txt')

def find(idx,tmp):
    if result[0] < tmp:
        return
    elif idx == N:
        result[0] = min(result[0],tmp)
    else:
        for i in range(idx,N):
            if not visited[i] and i != idx:
                visited[i] = 1
                find(idx+1,tmp+path[idx][i])
                visited[i] = 0

T = int(input())
for t in range(1,T+1):
    N = int(input())
    path = [list(map(int,input().split())) for _ in range(N)]
    visited = [0]*N
    visited[0] = 1
    result = [10000]
    find(0,0)
    print(result[0])