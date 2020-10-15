import sys
sys.stdin = open('input.txt')

def find(i):
    if i in visited:
        return 1
    elif data.get(i):
        visited.add(i)
        res.update(data[i])
        for j in data[i]:
            find(j)
        return 2
    else:
        return 3

test = int(input())
for t in range(1,test+1):
    N,M = map(int,input().split())
    data = {}
    visited = set()
    result = []

    for i in range(M):
        x,y = map(int,input().split())
        if data.get(x):
            data[x].append(y)
        else:
            data[x] = [y]
        if data.get(y):
            data[y].append(x)
        else:
            data[y] = [x]

    for i in range(1,N+1):
        res = set()
        x = find(i)
        if x == 1:
            continue
        elif x == 2:
            result.append(res)
        else:
            result.append({i})

    print(result)
    print(f'#{t} {len(result)}')