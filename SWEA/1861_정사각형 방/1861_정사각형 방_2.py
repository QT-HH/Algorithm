import sys
sys.stdin = open('input.txt')

import collections

di = [-1,0,1,0]
dj = [0,1,0,-1]
direct = [d for d in zip(di,dj)]
test = int(input())
for t in range(1,test+1):
    N = int(input())
    board = [list(map(int,input().split())) for _ in range(N)]
    maxVal = [10000,0]
    q = collections.deque()
    visited = set()

    for i in range(N):
        for j in range(N):
            for d in direct:
                ci = i+d[0]
                cj = j+d[1]
                if 0 <= ci < N and 0 <= cj < N:
                    if board[i][j] - board[ci][cj] == 1:
                        break
            else:
                q.append(((i,j),(i,j),1))

    while q:
        root, now, cnt = q.popleft()
        tmp = []
        for d in direct:
            i = now[0]+d[0]
            j = now[1]+d[1]
            if 0<=i<N and 0<=j<N:
                if board[now[0]][now[1]]-board[i][j]==-1:
                    tmp.append((root,(i,j),cnt+1))
        if tmp:
            q.extend(tmp)
        else:
            if maxVal[1] < cnt or (maxVal[1] == cnt and maxVal[0] > board[root[0]][root[1]]):
                maxVal[0] = board[root[0]][root[1]]
                maxVal[1] = cnt

    print(f'#{t} {maxVal[0]} {maxVal[1]}')