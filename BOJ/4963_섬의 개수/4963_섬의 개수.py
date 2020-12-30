import sys
sys.stdin = open('input.txt')

def dfs(i,j):
    stack = [(i,j)]
    while stack:
        p,q = stack.pop()
        for d in direct:
            y = p+d[0]
            x = q+d[1]
            if 0<= y <h and 0<= x <w and not check[y][x]:
                check[y][x] = True
                if field[y][x]:
                    stack.append((y,x))

direct = [(-1,0),(-1,1),(0,1),(1,1),(1,0),(1,-1),(0,-1),(-1,-1)]
while True:
    w,h = map(int,sys.stdin.readline().split())
    if w == 0:
        break

    field = []
    for _ in range(h):
        field.append([*map(int,sys.stdin.readline().split())])
    check = [[False]*w for _ in range(h)]

    cnt = 0
    for i in range(h):
        for j in range(w):
            if not check[i][j] and field[i][j]:
                dfs(i,j)
                cnt += 1
    print(cnt)