import sys
sys.stdin = open('input.txt')

def bfs():
    for i in range(R):
        for j in range(C):
            if field[i][j] == 'W':
                for d in direct:
                    y = i + d[0]
                    x = j + d[1]
                    if 0<= y <R and 0<= x <C:
                        if field[y][x] == 'S':
                            return 0
                        elif field[y][x] == '.':
                            field[y][x] = 'D'
    return 1

R,C = map(int,sys.stdin.readline().split())
field = []
for _ in range(R):
    field.append(list(sys.stdin.readline().rstrip()))

direct = [(-1,0),(0,1),(1,0),(0,-1)]
res = bfs()
print(res)
if res:
    for i in field:
        print(''.join(i))