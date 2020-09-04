import sys
sys.stdin = open('input.txt')

def find_start():
    for i in range(16):
        for j in range(16):
            if maze[i][j] == '2':
                return i,j

def find(q):
    q.append(find_start())
    while q:
        now1,now2 = q.popleft()
        visited[now1][now2] = 1
        for d in direct:
            after1 = now1+d[0]
            after2 = now2+d[1]
            if 0 <= after1 < 16 and 0 <= after2 < 16:
                if visited[after1][after2]:
                    continue
                elif maze[after1][after2]=='1':
                    continue
                elif maze[after1][after2]=='3':
                    return 1
                else:
                    q.append((after1,after2))
    return 0

import collections

di = [-1,0,1,0]
dj = [0,1,0,-1]
direct = [x for x in zip(di,dj)]
for _ in range(1,11):
    t = int(input())
    maze = [list(input()) for i in range(16)]
    visited = [[0]*16 for i in range(16)]
    Q = collections.deque()
    print(f'#{t} {find(Q)}')