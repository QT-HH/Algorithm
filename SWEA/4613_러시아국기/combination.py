def comb(v,s,res):
    if v == m:
        result.append(tuple(res))
    else:
        for i in range(s,n):
            res[v] = i
            comb(v+1,i+1,res)

n = 5
m = 2
result = []
res = [0]*m
comb(0,1,res)
print(result)

