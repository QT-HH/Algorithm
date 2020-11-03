import sys
sys.stdin = open('input.txt')

def find(now, before):
    # 남아있는 경로를 이미 방문한 적이 있음
    if dp[now][before]:
        return dp[now][before]

    # 모두 방문한 경우
    if before == (1 << (N+1)) - 1:
        return abs(comp[now][0]-house[0]) + abs(comp[now][1]-house[1])

    # 현재 지점에서 이동할 수 있는 지점들을 탐색
    cost = 999999
    for i in range(1, N+1):
        if not (before >> i) % 2 and path[now][i]:
            # i부터 0까지 순회를 만든 최소 비용
            tmp = find(i, before | (1 << i))  # before | (1<<i) == before + (1<<i)
            # (now~i), (i~0)의 합과 현재까지의 최소 비용과 비교
            cost = min(cost, tmp + path[now][i])

    # 메모이제이션
    dp[now][before] = cost
    return cost


T = int(input())
for t in range(1,T+1):
    N = int(input())
    homes = list(map(int,input().split()))
    comp = [[homes[0],homes[1]]]
    house = [homes.pop(2),homes.pop(2)]
    for i in range(2,len(homes),2):
        comp.append([homes[i],homes[i+1]])
    path = [[0]*(N+1) for _ in range(N+1)]

    for i in range(0,(N+1)*2,2):
        for j in range(0,(N+1)*2,2):
            if i != j:
                path[i//2][j//2] = abs(homes[i]-homes[j]) + abs(homes[i+1]-homes[j+1])

    dp = [[0]*(1<<(N+1)) for _ in range(N+1)]

    print('#{} {}'.format(t,find(0,1)))
