import sys
sys.stdin = open('input.txt')
input = sys.stdin.readline

def dfs():
    board = [input().rstrip() for _ in range(R)]
    stack = {(0, 0, board[0][0])}
    check = [[''] * C for _ in range(R)]
    res = 1

    while stack:
        i, j, visited = stack.pop()
        res = max(res, len(visited))
        if res == 26:
            return 26
        for d in direct:
            ny = i + d[0]
            nx = j + d[1]
            if 0 <= ny < R and 0 <= nx < C and board[ny][nx] not in visited:
                tmp = visited + board[ny][nx]
                if check[ny][nx] != tmp:
                    check[ny][nx] = tmp
                    stack.add((ny, nx, tmp))


    return res

y = (-1,0,1,0)
x = (0,1,0,-1)
direct = [(dy,dx) for dy,dx in zip(y,x)]
R,C = map(int,input().rstrip().split())

print(dfs())