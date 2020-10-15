import sys
sys.stdin = open('input.txt')

def dfs(root,idx,now,cnt):
    visited.add(idx)
    for d in direct:
        i = idx[0]+d[0]
        j = idx[1]+d[1]
        if 0<= i <N and 0<= j <N:
            if (i,j) in visited or (i,j) in donotgo:
                continue
            elif board[idx[0]][idx[1]] - board[i][j] == 1:
                print(visited)
                print(board[idx[0]][idx[1]],board[i][j])
                return

    for d in direct:
        i = idx[0] + d[0]
        j = idx[1] + d[1]
        if (i,j) in visited:
            continue
        elif 0<= i <N and 0<= j <N:
            if now-board[i][j]==-1:
                dfs(root,(i,j),board[i][j],cnt+1)

    if cnt > maxVal[1] or (cnt == maxVal[1] and root < maxVal[0]):
        maxVal[0] = root
        maxVal[1] = cnt

di = [-1,0,1,0]
dj = [0,1,0,-1]
direct = [d for d in zip(di,dj)]
test = int(input())
for t in range(1):
    N = int(input())
    board = [list(map(int,input().split())) for _ in range(N)]
    maxVal = [10000,0]
    donotgo = set()

    for i in range(N):
        for j in range(N):
            visited = set()
            dfs(board[i][j],(i,j),board[i][j],1)
            donotgo.add((i,j))

    print(f'#{t} {maxVal[0]} {maxVal[1]}')
