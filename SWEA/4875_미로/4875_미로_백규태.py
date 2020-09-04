import sys
sys.stdin = open('input.txt')

def find(i,j):
    start = maze[i][j]
    for d in direct:
        if 0 <= i+d[0] <N and 0 <= j+d[1] < N:
            if maze[i+d[0]][j+d[1]]==0:
                maze[i+d[0]][j+d[1]] = 1
                find(i+d[0],j+d[1])
            elif maze[i+d[0]][j+d[1]]==3:
                result[0] = 1
    return

di = [-1,0,1,0]
dj = [0,1,0,-1]
direct = [x for x in zip(di,dj)]
test = int(input())
for t in range(1,test+1):
    N = int(input())
    maze = [list(map(int,input())) for _ in range(N)]
    result = [0]

    for i in range(N):
        for j in range(N):
            if maze[i][j] == 2:
                find(i,j)

    print(f'#{t} {result[0]}')