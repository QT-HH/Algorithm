import sys
sys.stdin = open('input.txt')

def adventure(i,j,history):

    if len(history) == K:
        visited.add(history)
        return

    for d in direct:
        y = i+d[0]
        x = j+d[1]
        if 0<=x<N and 0<=y<N:
            adventure(y,x,history+board[y][x])

N = 4
K = 7
di = [-1,0,1,0]
dj = [0,1,0,-1]
direct = [x for x in zip(di,dj)]
test = int(input())
for t in range(1,test+1):
    visited = set()
    board = [input().split() for _ in range(N)]
    for i in range(N):
        for j in range(N):
            adventure(i,j,board[i][j])



    print(len(visited))