import sys
sys.stdin = open('input.txt')

def find():
    i = 0
    cnt = 0
    while i < N:
        max_go = 0
        for j in range(i+K, i, -1):
            if j in charge:
                max_go = j-i
                break
            elif i+K >= N:
                return cnt
        else:
            return 0

        i += max_go
        cnt +=1

    return 0




T = int(input())
for t in range(1,T+1):
    K,N,M = map(int,input().split())
    charge = list(map(int,input().split()))

    print('#{} {}'.format(t,find()))