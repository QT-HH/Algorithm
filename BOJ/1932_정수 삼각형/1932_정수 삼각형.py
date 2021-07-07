import sys
sys.stdin = open('input.txt')
input = sys.stdin.readline

n = int(input().rstrip())
pyramid = [[*map(int, input().rstrip().split())] for _ in range(n)]
c_pyramid = [l[:] for l in pyramid]

for f in range(len(pyramid)-1):
    for i in range(len(pyramid[f])):
        pyramid[f+1][i] = max(c_pyramid[f+1][i] + pyramid[f][i], pyramid[f+1][i])
        pyramid[f+1][i+1] = max(c_pyramid[f+1][i+1] + pyramid[f][i], pyramid[f+1][i+1])

print(max(pyramid[-1]))