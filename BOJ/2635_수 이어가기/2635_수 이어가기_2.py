import sys
sys.stdin=open('input.txt')

N = int(input())
arr = [N]
result = []
for i in range(1,N-1):
    arr.append(i)
    arr.append(arr[i-1]-arr[i])
    if arr[i+1] < 0:
        break
    else:
        arr.append(arr[i+1])
print(len(arr))
print(result)