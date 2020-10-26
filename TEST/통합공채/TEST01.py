import sys
sys.stdin = open('input.txt')

N = int(input())
arr = []
for i in range(N):
    arr.append(int(input()))

x = sum(arr)
res = x+1
idx = 0
for i in range(1,len(arr)-1):
    print(x-arr[i])
    if x-arr[i] < res:
        res = x-arr[i]
        idx = i

print(idx)