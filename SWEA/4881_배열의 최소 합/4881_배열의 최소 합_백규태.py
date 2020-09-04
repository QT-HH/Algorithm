import sys
sys.stdin = open('input.txt')

def arr_sum(row):
    if sub_res[0] > result[0]:
        return
    elif row == N:
        if sub_res[0] < result[0]:
            result[0] = sub_res[0]
        return

    for i in range(N):
        if visited[i] == True:
            continue
        else:
            visited[i] = True
            sub_res[0]+=arr[row][i]
            arr_sum(row+1)
            visited[i] = False
            sub_res[0]-=arr[row][i]


test = int(input())
for t in range(1,test+1):
    N = int(input())
    arr = [list(map(int,input().split())) for _ in range(N)]
    result = [100000]
    sub_res = [0]
    visited = [False]*N
    arr_sum(0)
    print(f'#{t} {result[0]}')