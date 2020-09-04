def judgement(i, j):
    x = [(i, j)]
    grid[i][j] = '.'
    while (1):
        temp = []
        for r, c in x:
            if c < column-1 and grid[r][c + 1] == '#':
                grid[r][c + 1] = '.'
                temp.append((r, c + 1))

            if c > 0 and grid[r][c - 1] == '#':
                grid[r][c - 1] = '.'
                temp.append((r, c - 1))

            if r < row-1 and grid[r + 1][c] == '#':
                grid[r + 1][c] = '.'
                temp.append((r + 1, c))

            if r > 0 and grid[r - 1][c] == '#':
                grid[r - 1][c] = '.'
                temp.append((r - 1, c))

        if temp == []:
            return 0
        else:
            x = temp[:]

import sys
sys.stdin = open('input.txt')
tc = int(input())
for _ in range(tc):
    row, column = map(int, input().split())
    grid = [list(input()) for i in range(row)]
    cnt = 0
    for i in range(row):
        for j in range(column):
            if grid[i][j] == '#':
                cnt += 1
                judgement(i, j)

    print(cnt)
