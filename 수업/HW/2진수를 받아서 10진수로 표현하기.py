x = list(map(int,' '.join(input()).split()))
res = []
for i in range(0,len(x),7):
    e = 1<<6
    tmp = 0
    for j in range(7):
        tmp += x[i+j]*e
        e>>=1
    res.append(tmp)

print(*res)