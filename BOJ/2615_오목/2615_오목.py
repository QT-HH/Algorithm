import sys
sys.stdin = open('input.txt')

def find(i,j,k):
    y = i + direct_none[k][0]
    x = j + direct_none[k][1]
    check = True
    if 0 <= x < 19 and 0 <= y < 19:
        if board[y][x] == board[i][j]:
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

        if 0 <= x < 19 and 0 <= y < 19:
            if board[y + direct[k][0]][x + direct[k][1]] == board[i][j]:
                return 0
            else:
                return board[i][j]
        else:
            return 0

def five():
    idx = []
    for i in range(19):
        for j in range(19):
            if board[i][j]:
                for k in range(3):
                    result = find(i, j, k)
                    if result:
                        idx = [i + 1, j + 1]
                        return result,idx

board = [list(map(int,input().split())) for _ in range(19)]

direct = [(0,1),(1,1),(1,0)]
direct_none = [(0,-1),(-1,-1),(-1,0)]
result = five()

print(result[0])
if len(result) > 1:
    print(*result[1])

