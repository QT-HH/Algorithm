# 파티션 : 전체를 두 부분으로 나누는 작업
# 퀵정렬 : 나누어진 두 각각 부분을 다시 퀵정렬
def partition(arr,start,end):
    # 피벗 선택하고 제일 앞쪽 값을 피벗으로 설정(피벗은 달라질 수 있다)
    pivot = arr[start]
    left = start+1
    right = end
    while left <= right:
        # left가 오른쪽으로 이동하며 피벗보다 큰 값을 찾기
        while left <= right and arr[left] >= pivot:
            if arr[left]==pivot:
            left += 1
        # right가 왼쪽으로 이동하며 피벗보다 작은 값을 찾기
        while left <= right and arr[right] <= pivot:
            right -= 1

        # 각각 큰 값과 작은 값을 찾았으면 위치교환
        if left < right:
            arr[left], arr[right] = arr[right], arr[left]

    arr[start], arr[right] = arr[right], arr[start]

    return right

def quick_sort(arr,start,end):
    # 파티션을 실행하고
    # 파티션으로 나누어진 부분을 각각 다시 퀵 소트
    if start < end:
        pivot = partition(arr,start,end)
        quick_sort(arr,start,pivot-1)
        quick_sort(arr,pivot+1,end)

    return

a = [1,3,2,5,6,8,2,4,6,9]
quick_sort(a,0,len(a)-1)
print(a)