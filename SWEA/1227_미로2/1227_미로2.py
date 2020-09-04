import sys
sys.stdin = open('input.txt')

import collections
di = [-1,0,1,0]
dj = [0,1,0,-1]
direct = [x for x in zip(di,dj)]
for t in range(1,11):
    test = int(input())
    maze = [list(input()) for _ in range(100)]
    result = 0

    for i in range(100):
        for j in range(100):
            if maze[i][j] == '2':
                start = (i,j)

    visited = {start}
    q = collections.deque()
    q.append(start)
    while q:
        x = q.popleft()
        for d in direct:
            i = x[0] + d[0]
            j = x[1] + d[1]
            if 0 <= i < 100 and 0<= j < 100:
                if (i,j) in visited:
                    continue
                elif maze[i][j] == '1':
                    continue
                elif maze[i][j] == '3':
                    result = 1
                    q.clear()
                    break
                else:
                    q.append((i,j))
                visited.add((i,j))

    print(f'#{t} {result}')