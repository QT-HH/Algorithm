import sys
sys.stdin = open('input.txt')

read = sys.stdin.readline
n = int(input())
arr = [[*map(int, read().split())] for _ in range(n)]
def func(a):
    return max(a[1:-1]),\
           max(a[0], a[2], a[4], a[5]),\
           max(a[0], a[1], a[3], a[5])
max_arr = [func(a) for a in arr]
ans = 0
d = {0:0, 1:1, 2:2, 3:1, 4:2, 5:0}
dd = {0:5, 1:3, 2:4, 3:1, 4:2, 5:0}
for i in range(6):
    a = arr[0][i]
    tmp = max_arr[0][d[i]]
    for j in range(1, n):
        jj = arr[j].index(a)
        tmp += max_arr[j][d[jj]]
        a = arr[j][dd[jj]]
    ans = max(ans, tmp)
print(ans)