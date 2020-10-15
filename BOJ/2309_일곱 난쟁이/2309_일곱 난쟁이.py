import sys
sys.stdin = open('input.txt')

def comb(base,cur,tmp):
    if base==2:
        x.append(tuple(tmp))
        return

    for i in range(cur,9):
        tmp[base] = height[i]
        comb(base+1,cur+1,tmp)

height = [int(input()) for _ in range(9)]
tmp = [0]*2
x = []
comb(0,0,tmp)
total = sum(height)
for i in x:
    if total-sum(i)==100:
        res = i
        break

result = []
for i in height:
    if i in res:
        continue
    else:
        result.append(i)

for i in sorted(result):
    print(i)