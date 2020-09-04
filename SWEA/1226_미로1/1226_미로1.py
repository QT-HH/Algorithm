# deqeu에 좌표 넣는 법을 모르겠음..

import sys
sys.stdin = open('input.txt')

def find_start():
    for i in range(16):
        for j in range(16):
            if maze[i][j] == '2':
                return [i,j]

def find(q):
    q.append(find_start())
    while q:
        now = q.pop(0)
        for d in direct:
            after = [now[0]+d[0],now[1]+d[1]]
            if 0 <= after[0] < 16 and 0 <= after[1] < 16:
                if maze[after[0]][after[1]]=='1':
                    continue
                elif maze[after[0]][after[1]]=='3':
                    return 1
                else:
                    maze[now[0]][now[1]] = '1'
                    q.append([after[0],after[1]])
    return 0

di = [-1,0,1,0]
dj = [0,1,0,-1]
direct = [x for x in zip(di,dj)]
for _ in range(1,11):
    t = int(input())
    maze = [list(input()) for i in range(16)]
    Q = []
    print(f'#{t} {find(Q)}')