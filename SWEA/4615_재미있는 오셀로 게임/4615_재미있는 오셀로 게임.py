import sys
sys.stdin = open('input.txt')

def check(N):
    for i in range(N):
        for j in range(N):
            if board[i][j]==0:
                for d in direction:
                    cnt=1
                    change = False
                    while 1:
                        if i + d[0] * cnt < 0 or i + d[0] * cnt > N - 1 or j + d[1] * cnt < 0 or j + d[1] * cnt > N - 1:
                            break
                        else:
                            if board[i+d[0]*cnt][j+d[1]*cnt]==0:
                                if change == True:
                                    return True
                                else:
                                    break
                            elif board[i+d[0]*cnt][j+d[1]*cnt] != board[i+d[0]*(cnt-1)][j+d[1]*(cnt-1)]:
                                change = True
                        cnt+=1


            else:
                continue
    return False

def go(i,j,color,d):
    cnt = 1
    while 1:
        if i+d[0]*cnt < 0 or i+d[0]*cnt > N-1 or j+d[1]*cnt < 0 or j+d[1]*cnt > N-1:
            return
        elif board[i+d[0]*cnt][j+d[1]*cnt] == 0:
            return
        elif board[i+d[0]*cnt][j+d[1]*cnt] == color:
            for c in range(cnt):
                board[i+d[0]*c][j+d[1]*c] = color
            return
        cnt += 1



test = int(input())
d_x = [-1,-1,0,1,1,1,0,-1]
d_y = [0,1,1,1,0,-1,-1,-1]
direction = [list(d) for d in zip(d_x,d_y)]

for t in range(1,test+1):
    N,M = map(int,input().split())
    board = [[0]*N for _ in range(N)]
    board[N // 2][N // 2] = 2
    board[N // 2 - 1][N // 2] = 1
    board[N // 2][N // 2 - 1] = 1
    board[N // 2 - 1][N // 2 - 1] = 2
    sig = False
    for m in range(M):
        if check(N) == True:
            sig = True
        if sig == False:
            break
        j,i,color = map(int,input().split())
        j-=1
        i-=1
        for d in direction:
            go(i,j,color,d)

    B = 0
    W = 0
    for i in range(N):
        for j in range(N):
            if board[i][j] == 1:
                B += 1
            elif board[i][j] == 2:
                W += 1

    print(f'#{t} {B} {W}')
