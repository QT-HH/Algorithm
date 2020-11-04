import sys

sys.stdin = open('input.txt')
from bisect import bisect

N = int(input())
poles = list(map(int, input().split()))
up = [poles[0]]
for i in range(1, N):
    if up[-1] < poles[i]:
        up.append(poles[i])
    else:
        idx = bisect(up, poles[i])
        up[idx] = poles[i]
print(N - len(up))
