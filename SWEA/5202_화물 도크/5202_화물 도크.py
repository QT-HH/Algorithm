import sys
sys.stdin = open('input.txt')

T = int(input())
for t in range(1,T+1):
    N = int(input())
    time = [list(map(int,input().split())) for _ in range(N)]
    time = sorted(time,key= lambda x: x[1])
    end = 0
    result = 0
    for i in time:
        if i[1] > end and i[0] >= end:
            result+=1
            end = i[1]

    print('#{} {}'.format(t,result))
