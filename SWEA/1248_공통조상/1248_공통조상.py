import sys
sys.stdin = open('input.txt')

import collections
test = int(input())
for t in range(1,test+1):
    V,E,x,y = map(int,input().split())
    data = list(map(int,input().split()))
    tree = {}
    tree2 = {}
    for i in range(0,len(data),2):
        tree[data[i+1]] = data[i]
        if tree2.get(data[i]):
            tree2[data[i]].append(data[i+1])
        else:
            tree2[data[i]] = [data[i+1]]
    visited = set()
    q = collections.deque()
    q.extend([x,y])
    result = 0
    while q:
        now = q.popleft()
        if tree.get(now):
            if tree[now] in visited:
                result = tree[now]
                q.clear()
            else:
                visited.add(tree[now])
                q.append(tree[now])

    q.append(result)
    cnt = 1
    while q:
        root = q.popleft()
        if tree2.get(root):
            for i in tree2[root]:
                q.append(i)
                cnt+=1

    print(f'#{t} {result} {cnt}')