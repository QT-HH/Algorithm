def minX(arr):
    tmp = []
    tot = 0

    for i in arr:
        tot+=i
        tmp.append(tot)

    x = 1-min(tmp)

    return x

arr = [-5,4,-2,3,1,-1,-6,-1,0,5]

print(minX(arr))