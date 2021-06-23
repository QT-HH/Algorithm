import sys
sys.stdin = open('input.txt')
input = sys.stdin.readline

T = int(input().rstrip())
k = int(input().rstrip())

coins = []
for _ in range(k):
    x,y = map(int,input().rstrip().split())
    coins.append((x,y))

result = [[0] * (k+1) for _ in range(T+1)]
result[0] = [1] * (k+1)

for i in range(1,k+1):
    v = coins[i-1][0]
    c = coins[i-1][1]

    for j in range(1, c+1):
        for q in range(v*j, T+1):
            result[q][i] += result[q-(v*j)][i-1]

    for j in range(1,T+1):
        result[j][i] += result[j][i-1]

print(result[-1][-1])

