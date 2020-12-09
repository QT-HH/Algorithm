import sys
sys.stdin = open('input.txt')

N,M = map(int,sys.stdin.readline().split())
market = {}
for _ in range(N):
    a,b = sys.stdin.readline().split()
    market[a] = int(b)

recipe = {}
for _ in range(M):
    a,b = sys.stdin.readline().rstrip().split('=')
    b = b.split('+')
    tmp = {}
    for i in range(len(b)):
        x = int(b[i][0])
        y = b[i][1:]
        if tmp.get(y):
            tmp[y] += x
        else:
            tmp[y] = x

    if recipe.get(a):
        recipe[a].append(tmp)
    else:
        recipe[a] = [tmp]


