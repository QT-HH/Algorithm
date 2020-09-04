def judgement(grid, i, j):
    x = [(i, j)]
    grid[i][j] = '.'
    while (1):
        temp = []
        for r, c in x:
            if grid[r][c + 1] == '#':
                grid[r][c + 1] = '.'
                temp.append((r, c + 1))

            if grid[r][c - 1] == '#':
                grid[r][c - 1] = '.'
                temp.append((r, c - 1))

            if grid[r + 1][c] == '#':
                grid[r + 1][c] = '.'
                temp.append((r + 1, c))

            if grid[r - 1][c] == '#':
                grid[r - 1][c] = '.'
                temp.append((r - 1, c))

        if temp == []:
            return 0
        else:
            x = temp[:]


tc = int(input())
for _ in range(tc):
    row, column = map(int, input().split())
    grid = [list('.' + input() + '.') for i in range(row)]
    grid.insert(0, ['.'] * (column + 2))
    grid.append(['.'] * (column + 2))

    cnt = 0
    for i in range(row + 2):
        for j in range(column + 2):
            if grid[i][j] == '#':
                cnt += 1
                judgement(grid, i, j)

    print(cnt)
