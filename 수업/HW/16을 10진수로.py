num = input()

hd = {
    'A':10,
    'B':11,
    'C':12,
    'D':13,
    'E':14,
    'F':15
}
for i in range(10):
    hd[str(i)] = i

r_res = []
for i in range(len(num)-1,-1,-1):
    x = hd[num[i]]
    for j in range(4):
        r_res.append(x%2)
        x //= 2

res = r_res[::-1]

result = []
for i in range(0,len(res),7):
    k = 1
    tot = 0
    for j in range(6,-1,-1):
        if i+j >= len(res):
            continue
        tot += res[i+j]*k
        k <<= 1
    result.append(tot)

print(*result)

# 01D06079861D79F99F
# 0F97A3