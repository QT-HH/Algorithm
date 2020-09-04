import sys
sys.stdin = open('input.txt')

def maze(nav,x):
    result = 0
    if nav.get(x):
        for i in nav[x]:
            if result>0:
                return 1

            if i in total:
                continue
            else:
                total.add(i)

            if i:
                result +=maze(nav,i)
            else:
                result = 1
    else:
        result = 0
    return result

for t in range(1,11):
    n, road = map(int,input().split())
    nav = {}
    x = list(map(int,input().split()))
    total=set()

    for i in range(len(x)-1,-1,-2):
        if nav.get(x[i]):
            nav[x[i]].append(x[i-1])
        else:
            nav[x[i]]=[x[i-1]]
    print(maze(nav,99))
