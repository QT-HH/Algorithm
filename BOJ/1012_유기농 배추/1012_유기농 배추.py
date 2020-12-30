import sys
sys.stdin = open('input.txt')

direct = [(-1,0),(0,1),(1,0),(0,-1)]

def dfs(i,j):
    stack = [(i,j)]
    while stack:
        p,q = stack.pop()
        check[p][q] = True
        for d in direct:
            y = p+d[0]
            x = q+d[1]
            if 0<= y <N and 0<= x <M and not check[y][x]:
                check[y][x] = True
                if field[y][x]:
                    stack.append((y,x))

T = int(sys.stdin.readline())
for t in range(T):
    M,N,K = map(int,sys.stdin.readline().split())
    field = [[0]*M for _ in range(N)]
    for _ in range(K):
        X,Y = map(int,sys.stdin.readline().split())
        field[Y][X] = 1

    check = [[False]*M for _ in range(N)]

    cnt = 0
    for i in range(N):
        for j in range(M):
            if not check[i][j] and field[i][j]:
                dfs(i,j)
                cnt+=1

    print(cnt)