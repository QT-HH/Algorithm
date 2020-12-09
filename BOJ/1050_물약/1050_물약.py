import sys
sys.stdin = open('input.txt')

def find(name):
    total = 0
    res = 1000000001
    flag = False
    if market.get(name):
        res = market[name]
        flag = True
    if exp.get(name):
        tmp = 0
        for i in exp[name]:
            for j in i:
                now = find(j)
                if now:
                    tmp += i[j] * now
                else:
                    break
            else:
                continue
            break
        else:
            res = min(res,tmp)
            flag = True


    if flag:
        if res > 1000000000:
            return 1000000001
        else:
            return res
    else:
        return -1



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
visited = set()
print(market)
print(exp)
# print(find('LOVE'))

