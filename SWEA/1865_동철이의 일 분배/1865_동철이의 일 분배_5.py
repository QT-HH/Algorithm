import sys
sys.stdin = open('input.txt')

def play(n):
    global result
    global re

    if n == N:
        rre = 1 * 10 ** -(N * 2 - 2)
        for i in range(N):
            rre *= p_stack[i]
        result = rre
    for wi in range(N):
        if visited_w[wi] == 0 and li_p[n][wi] != 0:
            if re * li_p[n][wi] * 10 ** -2 < result:
                continue
            visited_w[wi] = 1
            re *= (li_p[n][wi] * 10 ** -2)
            p_stack.append(li_p[n][wi])
            play(n + 1)
            re /= (li_p[n][wi] * 10 ** -2)
            visited_w[wi] = 0
            p_stack.pop()


T = int(input())

for TC in range(1, T + 1):
    N = int(input())

    li_p = []
    for _ in range(N):
        li_p.append(list(map(int, input().split())))
    result = 0
    re = 100
    p_stack = []
    visited_w = [0] * N
    play(0)
    print('#%d %.6f' % (TC, result))