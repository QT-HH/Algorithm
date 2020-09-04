import sys
sys.stdin = open('input.txt')

def maze(nav,x):
    result = 0
    if nav.get(x):
        for i in nav[x]:
            if i in total:
                continue
            else:
                total.add(i)

            if i == 99:
                result = 1
            else:
                result += maze(nav,i)
    else:
        return 0
    return result

for t in range(1,11):
    n, road = map(int,input().split())
    nav = {}
    x = list(map(int,input().split()))
    total=set()

    for i in range(len(x)):
        if i%2:
            nav[x[i-1]].append(x[i])
        elif nav.get(x[i]):
            continue
        else:
            nav[x[i]]=[]
    # res = 1 if maze(nav,0) else 0
    print(f'#{t} {maze(nav,0)}')
