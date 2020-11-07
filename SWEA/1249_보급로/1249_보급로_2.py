import heapq
dr = [0,1,0,-1]
dc = [1,0,-1,0]
for tc in range(1, int(input())+1):
    N = int(input())
    pan = [list(map(int,input())) for _ in range(N)]
    D = [[0xffff]*N for _ in range(N)]
    visited = [[False]*N for _ in range(N)]
    q = []
    heapq.heappush(q, (0,0,0))
    D[0][0] = 0
    while q:
        d,r,c = heapq.heappop(q)
        if visited[r][c]: continue
        visited[r][c] = True
        for i in range(4):
            nr = r+dr[i]
            nc = c+dc[i]
            if 0<=nr<N and 0<=nc<N and D[nr][nc] > D[r][c]+pan[nr][nc]:
                D[nr][nc] = D[r][c]+pan[nr][nc]
                heapq.heappush(q,(D[nr][nc],nr,nc))
    print("#{} {}".format(tc, D[N-1][N-1]))