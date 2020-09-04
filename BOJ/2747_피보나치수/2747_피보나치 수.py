n = int(input())
x = [0,1]
for i in range(2,n+1):
    x.append(x[i-1]+x[i-2])

print(x[n])