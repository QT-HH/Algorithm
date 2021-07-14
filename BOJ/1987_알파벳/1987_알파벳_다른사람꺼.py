import sys
sys.stdin = open('input.txt')
input = sys.stdin.readline

y = (-1,0,1,0)
x = (0,1,0,-1)
direct = [(dy,dx) for dy,dx in zip(y,x)]

R,C = map(int,input().rstrip().split())
board = [list(input().rstrip()) for _ in range(R)]
q = {(0,0,board[0][0])}
check = [['']*C for _ in range(R)]
res = 1

while q:
    i, j, visited = q.pop()
    for d in direct:
        ny = i+d[0]
        nx = j+d[1]
        if 0<=ny<R and 0<=nx<C and board[ny][nx] not in visited:
            tmp = visited+board[ny][nx]
            if check[ny][nx] != tmp:
                check[ny][nx] = tmp
                q.add((ny,nx,tmp))
            res = max(res,len(tmp))
    if res == 26:
        break

print(res)