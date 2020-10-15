import sys
sys.stdin = open('input.txt')

N = int(input())
K = int(input())
data = [tuple(map(int,input().split())) for _ in range(K)]

if N%2:
    x = N // 2 + 1
else:
    x = N//2

for j, i in data:
    if j > x:
        j = N - j + 1
    if i > x:
        i = N - i + 1
    c_idx = min(i, j)
    color = c_idx % 3
    if color:
        print(color)
    else:
        print(3)