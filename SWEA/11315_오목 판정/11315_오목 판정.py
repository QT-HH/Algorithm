import sys
sys.stdin = open('input.txt')

def check():
    for i in range(N):
        for j in range(N):
            if board[i][j] == 'o':
                for di,dj in direct:
                    for c in range(1,5):
                        y = i+di*c
                        x = j+dj*c
                        if 0 <= y < N and 0 <= x < N and board[y][x] == 'o':
                            continue
                        else:
                            break
                    else:
                        return 'YES'

    return 'NO'

direct = [(0,1),(1,1),(1,0),(1,-1)]
T = int(input())
for t in range(1,T+1):
    N = int(input())
    board = [input() for _ in range(N)]
    res = check()

    print('#{} {}'.format(t,res))
