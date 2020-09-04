import sys
sys.stdin = open('input.txt')

def find():
    q = [S]
    visited = {S}
    cnt = 0
    while q:
        tmp = []
        cnt+=1
        for node in q:
            if graph.get(node) ==None:
                continue
            for i in graph[node]:
                if i in visited:
                    continue
                elif i == G:
                    return cnt
                else:
                    visited.add(i)
                    tmp.append(i)
        q = tmp
    return 0


test = int(input())
for t in range(1,test+1):
    graph = {}
    V,E = map(int,input().split())
    for i in range(E):
        fr, to = map(int,input().split())
        if graph.get(fr):
            graph[fr].append(to)
        else:
            graph[fr] = [to]
        if graph.get(to):
            graph[to].append(fr)
        else:
            graph[to] = [fr]
    S, G = map(int,input().split())
    print(f'#{t} {find()}')
