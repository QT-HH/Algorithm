import sys
sys.stdin = open('input1.txt')

K = int(input())
arr = [K]
temp = []
new_arr = []
# 임시 리스트에 K-1까지의 수를 넣는다.
for k in range(1, K):
    temp.append(k)
# 두번째 순서를 랜덤으로 결정(for문으로 1부터 99까지)
for i in range(K - 1):
    arr = [K]
    # 두번째 들어갈 숫자를 임시 리스트에서 뽑아 넣는다.
    sec_n = temp.pop()
    arr.append(sec_n)
    for j in range(30000):
        thr_num = arr[len(arr) - 2] - arr[len(arr) - 1]
        if thr_num >= 0:
            arr.append(thr_num)
    new_arr.append(arr)

# 최대 길이 구하기
max_cnt = 0
save = 0
for i in range(len(new_arr)):
    cnt = 0
    for j in range(len(new_arr[i])):
        cnt += 1
    if max_cnt < cnt:
        max_cnt = cnt
        if len(new_arr[i]) == max_cnt:
            save = new_arr[i]

print(max_cnt)
print(*save)