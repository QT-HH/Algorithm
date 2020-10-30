import sys
sys.stdin = open('input.txt')

def solve(N, P):
    res = 0

    def dfs(n, total):
        nonlocal res
        if total <= res:
            return

        if n == N:
            res = max(total, res)
            return

        for i in range(N):
            if visit[i]:
                continue
            visit[i] = True
            dfs(n + 1, total * P[n][i] / 100)
            visit[i] = False

    visit = [False] * N
    dfs(0, 1)

    return res


if __name__ == '__main__':

    T = int(input())

    for t in range(1, T + 1):
        N = int(input())

        P = [[*map(int, input().split())] for _ in range(N)]

        answer = solve(N, P)

        answer *= 100

        print('#%d %.6f' % (t, answer))