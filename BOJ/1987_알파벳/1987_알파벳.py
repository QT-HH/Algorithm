import sys
sys.stdin = open('input.txt')
input = sys.stdin.readline

def dfs(i, j, n):

    res[0] = max(res[0], n)

    for d in direct:
        ny = i+d[0]
        nx = j+d[1]
        if 0<=ny<R and 0<=nx<C and not check[board[ny][nx]]:
            check[board[ny][nx]] = True
            dfs(ny, nx, n+1)
            check[board[ny][nx]] = False

dy = (-1,0,1,0)
dx = (0,1,0,-1)
direct = [(y,x) for y,x in zip(dy,dx)]

alphabets = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
check = dict()
for a in alphabets:
    check[a] = False

R,C = map(int,input().rstrip().split())
board = [input().rstrip() for _ in range(R)]
res = [0]
check[board[0][0]] = True
dfs(0,0,1)
print(res[0])
