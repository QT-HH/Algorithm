import sys
sys.stdin = open('input.txt')


for test in range(1,11):
    t, k = map(int, input().split())
    roads = list(map(int,input().split()))
    x = {}
    visited=set()
    result = 0
    for i in range(0,len(roads)-1,2):
        if x.get(roads[i]):
            x[roads[i]].append(roads[i+1])
        else:
            x[roads[i]]=[roads[i+1]]

    stack = []
    stack.extend(x[0])
    while stack:
        a = stack.pop()
        if a in visited:
            continue
        else:
            visited.add(a)

        if a == 99:
            result = 1
            break
        elif x.get(a)==None:
            continue
        else:
            stack.extend(x[a])

        # if a not in visited:
        #     visited.add(a)
        #     if a==99:
        #         result = 1
        #         break
        #     elif x.get(a)==None:
        #         continue
        #     else:
        #         stack.extend(x.get(a))
        # else:
        #     continue

    print(f'#{t} {result}')