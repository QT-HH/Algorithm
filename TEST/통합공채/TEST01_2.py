import sys
sys.stdin = open('input.txt')

N = int(input())
arr = []
for i in range(N):
    arr.append(int(input()))

tot = 0
tmp = []
for i in range(len(arr)):
    tot+=arr[i]
    tmp.append(tot)

x = tmp[-1]+1
idx = 0
for i in range(1,len(arr)-1):
    r = tmp[-1] - tmp[i]
    l = tmp[i-1]

    if 0 <= r-l < x:
        x = r-l
        idx = i

print(x)
print(idx)