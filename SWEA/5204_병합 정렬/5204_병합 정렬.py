import sys
sys.stdin = open('input.txt')

def sum_sort(array):
    if len(array) == 1:
        return array

    c = len(array)//2
    l_array = sum_sort(array[:c])
    r_array = sum_sort(array[c:])

    if l_array[-1] > r_array[-1]:
        cnt[0] += 1

    new_array = []
    i = 0
    j = 0
    l_len = len(l_array)
    r_len = len(r_array)
    while len(new_array) < l_len + r_len:

        if i == l_len:
            new_array.append(r_array[j])
            j += 1
        elif j == r_len:
            new_array.append(l_array[i])
            i += 1
        elif l_array[i] < r_array[j]:
            new_array.append(l_array[i])
            i += 1
        else:
            new_array.append(r_array[j])
            j += 1

    return new_array

T = int(input())
for t in range(1,T+1):
    N = int(input())
    numbers = list(map(int,input().split()))
    cnt = [0]
    result = sum_sort(numbers)

    print('#{} {} {}'.format(t,result[N//2],cnt[0]))
