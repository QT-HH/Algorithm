import sys
sys.stdin = open('input.txt')

def find(name):
    tmp = 101
    if cost.get(name):
        return cost[name]

    if market.get(name):
        tmp = market[name]
    if exp.get(name):
        for i in exp[name]:
            x = 0
            for j in i:
                x += find(j)
            tmp = min(tmp,x)

    cost[name] = tmp
    return tmp


N,M = map(int,input().split())
market = {}
for i in range(N):
    x,y = sys.stdin.readline().split()
    market[x] = int(y)

exp = {}
for i in range(M):
    x,y = sys.stdin.readline().rstrip().split('=')
    mat = y.split('+')
    material = {}
    for j in range(len(mat)):
        num = int(mat[j][0])
        name = mat[j][1:]
        if material.get(name):
            material[name]+=num
        else:
            material[name] = num

    if exp.get(x):
        exp[x].append(material)
    else:
        exp[x] = [material]

cost = {}
res = 0
for i in exp['LOVE']:
    find(i)
