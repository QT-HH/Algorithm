import sys
sys.stdin = open('input.txt')

def merge_sort(arr):
    if len(arr) <= 1:
        return arr

    mid = len(arr)//2
    left = arr[:mid]
    right = arr[mid:]

    left1 = merge_sort(left)
    right1 = merge_sort(right)
    return merge(left1, right1)


def merge(left, right):
    global cnt
    i = 0
    j = 0
    sorted_arr = []

    if left[-1] > right[-1]:
        cnt += 1

    while (i < len(left)) & (j < len(right)):
        if left[i] < right[j]:
            sorted_arr.append(left[i])
            i += 1
        else:
            sorted_arr.append(right[j])
            j += 1

    while i < len(left):
        sorted_arr.append(left[i])
        i += 1

    while j < len(right):
        sorted_arr.append(right[j])
        j += 1

    return sorted_arr


for tc in range(1, int(input())+1):
    N = int(input())
    arr = list(map(int, input().split()))
    cnt = 0
    a = merge_sort(arr)
    print(f'#{tc} {a[N//2]} {cnt}')