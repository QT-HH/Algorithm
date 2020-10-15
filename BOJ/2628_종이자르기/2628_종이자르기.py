import sys
sys.stdin = open('input.txt')

r, c = map(int, input().split())
n = int(input())
paper = [[0] * r for _ in range(c)]
# print(paper)
for i in range(n):
    a, b = map(int, input().split())
    if a == 0:
        for x in range(r):
            paper[b-1][x] = 1
    if a == 1:
        for y in range(c):
            paper[y][b-1] = 1
for i in paper:
    print(i)
cnt = 0
row = []
for i in range(r):
    if paper[0][i] == 0:
        cnt += 1
    if i == (r-1):
        row.append(cnt)
        break
    if paper[0][i] == 1:
        cnt+=1
        row.append(cnt)
        cnt = 0
        continue
a = max(row)
cnt = 0
col = []
for i in range(c):
    if paper[i][0] == 0:
        cnt += 1
    if i == (c-1):
        col.append(cnt)
        break
    if paper[i][0] == 1:
        cnt+=1
        col.append(cnt)
        cnt = 0
        continue
b = max(col)
print(row)
print(col)
print(a*b)