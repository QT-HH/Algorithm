import sys
sys.stdin = open('input.txt')
input = sys.stdin.readline

N = int(input().rstrip())
times = sorted([[*map(int,input().rstrip().split())] for _ in range(N)], key=lambda x: (x[1], x[0]))
res = 0

start = -1
end = -1
for s,e in times:
    if end <= s:
        res += 1
        start = s
        end = e

print(res)




