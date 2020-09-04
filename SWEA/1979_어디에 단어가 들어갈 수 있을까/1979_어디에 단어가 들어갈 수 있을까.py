import sys
sys.stdin = open('input.txt')

test = int(input())
for t in range(1,test+1):
    N,K = map(int,input().split())
    data = [list(map(int,input().split())) for _ in range(N)]
    res = 0

    for i in range(N):
        count_r=0
        count_c=0
        for j in range(N):
            if data[i][j]:
                count_r+=1
            else:
                if count_r==K:
                    res+=1
                count_r = 0
            if data[j][i]:
                count_c+=1
            else:
                if count_c==K:
                    res+=1
                count_c = 0
        else:
            if count_r==K:
                res+=1
            if count_c==K:
                res+=1

    print(f'#{t} {res}')