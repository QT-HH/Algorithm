import sys
sys.stdin = open('input.txt')

def find(now, before):
    # 남아있는 경로를 이미 방문한 적이 있음
    if dp[now][before]:
        return dp[now][before]

    # 모두 방문한 경우
    if before == (1 << n) - 1:
        return path[now][0] if path[now][0] > 0 else max_size

    # 현재 지점에서 이동할 수 있는 지점들을 탐색
    cost = max_size
    for i in range(1, n):
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
    n = int(sys.stdin.readline())
    path = [list(map(int, sys.stdin.readline().split())) for _ in range(n)]
    max_size = 0
    for i in path:
        max_size += sum(i)
    dp = [[0] * (1 << n) for _ in range(n)]

    print('#{} {}'.format(t,find(0, 1)))