import sys
sys.stdin = open('input.txt')
input = sys.stdin.readline

def find_son(start, fuel):
    q = [start]
    visited = {start}
    cand = []
    cnt = 0

    if start in son and son[start]:
        return (start, fuel)

    while True:
        cnt += 1
        tmp = []
        while q:
            now = q.pop()
            for d in direct:
                y = now[0]+d[0]
                x = now[1]+d[1]
                if 0<=y<N and 0<=x<N and not board[y][x]:
                    if (y,x) in visited:
                        continue
                    elif (y,x) in son and son[(y,x)]:
                        cand.append((y,x))
                    else:
                        tmp.append((y,x))
                    visited.add((y,x))

        if cand:
            if fuel < cnt:
                return -1
            else:
                return (sorted(cand)[0], fuel-cnt)
        elif tmp:
            q = tmp
        else:
            return -1

def find_det(start,fuel):
    q = [start]
    visited = {start}
    cnt = 0
    while True:
        cnt += 1
        tmp = []
        while q:
            now = q.pop()
            for d in direct:
                y = now[0] + d[0]
                x = now[1] + d[1]
                if 0 <= y < N and 0 <= x < N and not board[y][x]:
                    if (y, x) in visited:
                        continue
                    elif (y, x) == son[start]:
                        if fuel < cnt:
                            return -1
                        else:
                            return ((y,x), fuel + cnt)
                    else:
                        tmp.append((y, x))
                    visited.add((y, x))

        if tmp:
            q = tmp
        else:
            return -1

dy = [-1,0,1,0]
dx = [0,1,0,-1]
direct = [i for i in zip(dy,dx)]

N,M,fuel = map(int,input().rstrip().split())
board = [[*map(int,input().rstrip().split())] for _ in range(N)]
now = tuple(map(lambda x: int(x)-1,input().rstrip().split()))
son = dict()
for _ in range(M):
    a,b,c,d = map(lambda x: int(x)-1,input().rstrip().split())
    son[(a,b)] = (c,d)

c = 0
while True:
    now_son = find_son(now,fuel)
    if now_son == -1:
        print(-1)
        break
    else:
        res = find_det(now_son[0], now_son[1])
        son[now_son[0]] = False
        if res == -1:
            print(-1)
            break
        else:
            c+=1
            now = res[0]
            fuel = res[1]

            if c >= len(son):
                print(res[1])
                break