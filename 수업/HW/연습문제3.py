# 0DEC
# 0269FAC9A0



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

password = {
    '001101':0,
    '010011':1,
    '111011':2,
    '110001':3,
    '100011':4,
    '110111':5,
    '001011':6,
    '111101':7,
    '011001':8,
    '101111':9,
}

def pw(code):

    r_res = []
    for i in range(len(code)-1,-1,-1):
        x = hd[code[i]]
        for j in range(4):
            r_res.append(str(x%2))
            x //= 2

    res = r_res[::-1]
    result = []
    d = 0
    for i in range(len(res)):
        k = ''.join(res[i:i+6])
        if password.get(k) != None:
            d = i
            break

    for i in range(d,len(res),6):
        k = ''.join(res[i:i + 6])
        if password.get(k) != None:
            result.append(password[k])

    return result


num = input()
print(*pw(num))