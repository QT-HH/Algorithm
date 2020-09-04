import sys
sys.stdin = open('input.txt')

def bfs(S,G):
    stack = road[S]
    while stack:
        a = stack.pop()
        if a in visited:
            continue
        else:
            visited.add(a)

        if road.get(a):
            for i in road[a]:
                if i == G:
                    return 1
                else:
                    stack.append(i)
        else:
            continue
    else:
        return 0


test = int(input())
for t in range(1,test+1):
    road = {}
    visited = set()
    result = 0
    V, E = map(int,input().split())
    for e in range(E):
        x,y = map(int,input().split())
        if road.get(x):
            road[x].append(y)
        else:
            road[x] = [y]

    S, G = map(int,input().split())

    print(f'#{t} {bfs(S,G)}')