import sys
sys.stdin = open('input.txt')

def adv(j):
    cnt = 0
    i = 0
    while i<99:
        if j>0 and ladder[i][j-1]:
            while j>0 and ladder[i][j-1]:
                j-=1
                cnt+=1
            i+=1
            cnt+=1
        elif j<99 and ladder[i][j+1]:
            while j<99 and ladder[i][j+1]:
                j+=1
                cnt+=1
            i+=1
            cnt+=1
        else:
            i+=1
            cnt+=1
    return cnt

for test in range(1,11):
    t = int(input())
    ladder = [list(map(int,input().split())) for _ in range(100)]
    min_cnt = 10001
    for start in range(100):
        if ladder[0][start]:
            cnt = adv(start)
            if min_cnt > cnt:
                min_cnt = cnt
                min_start = start
    print(f'#{t} {min_start}')