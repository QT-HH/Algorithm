import sys
sys.stdin = open('input.txt')

def find(now,visited):
    if dp[now][visited]:
        return dp[now][visited]

    if visited == (1<<N)-1:
        return graph[now][0] if graph[now][0]>0 else sys.maxsize

    cost = sys.maxsize
    for i in range(N):
        if not (visited>>i) % 2 and graph[now][i]:
            tmp = find(i,visited|(1<<i))
            cost = min(cost,tmp+graph[now][i])

    dp[now][visited] = cost
    return cost

N = int(input())
graph = [list(map(int,input().split())) for _ in range(N)]
dp = [[0]*(1<<N) for _ in range(N)]
print(find(0,1))