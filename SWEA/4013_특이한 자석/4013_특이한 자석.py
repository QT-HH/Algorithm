import sys
sys.stdin = open('input.txt')

from collections import deque

T = int(input())
for t in range(1,T+1):
    K = int(input())
    magnets = [deque(map(int,input().split())) for _ in range(4)]
    rotate = [list(map(int,input().split())) for _ in range(K)]

    for i in rotate:
        m = i[0]-1
        rot = i[1]
        r = [False]*4
        r[m] = rot

        for j in range(m,3):
            if magnets[j][2] != magnets[j+1][6]:
                if r[j] == -1:
                    r[j+1] = 1
                elif r[j] == 1:
                    r[j+1] = -1
            else:
                break

        for j in range(m,0,-1):
            if magnets[j][6] != magnets[j-1][2]:
                if r[j] == -1:
                    r[j-1] = 1
                elif r[j] == 1:
                    r[j-1] = -1
            else:
                break

        for j in range(4):
            if r[j]==1:
                x = magnets[j].pop()
                magnets[j].appendleft(x)
            elif r[j]==-1:
                x = magnets[j].popleft()
                magnets[j].append(x)


    tmp = 1
    score = 0
    for i in range(4):
        if magnets[i][0]:
            score+=tmp
        tmp*=2

    print('#{} {}'.format(t,score))
