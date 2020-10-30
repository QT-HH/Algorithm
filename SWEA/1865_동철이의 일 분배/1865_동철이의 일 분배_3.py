import sys
sys.stdin = open('input.txt')

def f2(n, k, s):
    global max_val
    if n == k:
        if max_val < s * 100:
            max_val = s * 100
        return
    elif max_val >= s * 100:
        return
    else:
        for i in range(n, k):
            p[n], p[i] = p[i], p[n]
            f2(n + 1, k, s * P[n][p[n]] / 100)
            print(p)
            p[n], p[i] = p[i], p[n]


T = int(input())
for tc in range(T):
    max_val = 0
    N = int(input())
    arr = [i for i in range(N)]
    P = [list(map(int, input().split())) for _ in range(N)]
    u = [0] * N
    p = [i for i in range(N)]
    f2(0, N, 1)
    print('#%d %.6f' % (tc + 1, round(max_val, 6)))