import sys
sys.stdin = open('input.txt')

import collections

def find_start():
    for i in range(N):
        for j in range(N):
            if maze[i][j] == '2':
                return i,j

def find(start):
    visited = {start}
    q = collections.deque()
    q.append(start)
    cnt = -1
    while q:
        tmp = []
        cnt+=1
        for now in q:
            for d in direct:
                i = now[0] + d[0]
                j = now[1] + d[1]
                if 0<=i<N and 0<=j<N:
                    if (i,j) in visited:
                        continue
                    elif maze[i][j] == '1':
                        visited.add((i,j))
                        continue
                    elif maze[i][j] == '3':
                        return cnt
                    else:
                        visited.add((i,j))
                        tmp.append((i,j))
        q.clear()
        q.extend(tmp)
    else:
        return 0

di = [-1,0,1,0]
dj = [0,1,0,-1]
direct = [x for x in zip(di,dj)]
test = int(input())
for t in range(1,test+1):
    N = int(input())
    maze = [list(input()) for _ in range(N)]
    print(f'#{t} {find(find_start())}')