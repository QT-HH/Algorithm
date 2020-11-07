import sys
sys.stdin = open('input.txt')

direct = [(-1,0),(0,1),(1,0),(0,-1)]
ptype = [(),(0,1,2,3),(0,2),(1,3),(0,1),(1,2),(2,3),(3,0)]
ctype = [(),(0,1,2,3),(0,2),(1,3),(2,3),(3,0),(0,1),(1,2)]

T = int(input())
for t in range(1,T+1):
    N,M,R,C,L = map(int,input().split())
    board = [[*map(int,input().split())] for _ in range(N)]

    visited = set()
    q = [(R,C)]
    while L:
        L-=1
        tmp = []
        for a,b in q:
            visited.add((a,b))
            for i in range(len(direct)):
                if i in ptype[board[a][b]]:
                    y = a + direct[i][0]
                    x = b + direct[i][1]
                    if 0<= y <N and 0<= x <M and board[y][x] != 0 and i in ctype[board[y][x]] and (y,x) not in visited:
                        tmp.append((y,x))
        q = tmp

    print('#{} {}'.format(t,len(visited)))

