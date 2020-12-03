import sys
sys.stdin = open('input.txt')

def bfs():
    long = 0
    for tp in tops:
        if board[tp[0]][tp[1]] < top:
            continue

        cnt = 0
        q = [tp]
        while q:
            cnt+=1

            tmp = []
            for step in q:
                for d in direct:
                    y = step[0]+d[0]
                    x = step[1]+d[1]
                    if 0<=x<N and 0<=y<N and board[y][x] < board[step[0]][step[1]]:
                        tmp.append((y,x))
            q = tmp
        long = max(long,cnt)

    return long

T = int(input())
for t in range(1,T+1):
    N,K = map(int,input().split())
    board = [list(map(int,input().split())) for _ in range(N)]

    top = 0
    tops = []
    for i in range(N):
        for j in range(N):
            if board[i][j] > top:
                tops = [(i,j)]
                top = board[i][j]
            elif board[i][j] == top:
                tops.append((i,j))

    direct = [(-1,0),(0,1),(1,0),(0,-1)]
    max_cnt = 0

    for i in range(N):
        for j in range(N):
            max_cnt = max(max_cnt, bfs())
            for k in range(K):
                board[i][j]-=1
                max_cnt = max(max_cnt,bfs())
            board[i][j]+=K

    print('#{} {}'.format(t,max_cnt))
