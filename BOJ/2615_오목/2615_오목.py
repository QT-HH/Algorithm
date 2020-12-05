import sys
sys.stdin = open('input.txt')

def find(i,j,k):
    y = i + direct_none[k][0]
    x = j + direct_none[k][1]
    check = True
    if 0 <= x < 19 and 0 <= y < 19 and board[y][x] == board[i][j]:
        check = False

    if check:
        for t in range(1, 5):
            y = i + direct[k][0] * t
            x = j + direct[k][1] * t
            if 0 <= x < 19 and 0 <= y < 19:
                if board[y][x] != board[i][j]:
                    return 0
            else:
                return 0

        if 0 <= y+direct[k][0] < 19 and 0 <= x+direct[k][1] < 19 and board[y + direct[k][0]][x + direct[k][1]] == board[i][j]:
            return 0

        return board[i][j]

    else:
        return 0

def five():
    idx = []
    res = 0
    for i in range(19):
        for j in range(19):
            if board[i][j]:
                for k in range(4):
                    res = find(i, j, k)
                    if res:
                        idx = [i + 1, j + 1]
                        return res,idx
    return [0]

board = [list(map(int,input().split())) for _ in range(19)]

direct = [(0,1),(1,1),(1,0),(-1,1)]
direct_none = [(0,-1),(-1,-1),(-1,0),(1,-1)]
result = five()

print(result[0])
if len(result) > 1:
    print(*result[1])

