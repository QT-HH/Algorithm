n = int(input())
x, y = 0, 1
for i in range(n):
    x,y = y, x+y
print(x)