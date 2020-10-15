import sys
sys.stdin = open('input.txt')

import collections

def find_des(taxi,des,fuel):
    q = collections.deque()
    q.append(taxi)
    visited = {taxi}
    cnt = 0
    while 1:
        cnt+=1
        fuel-=1
        if fuel!=-1:
            tmp = []
            while q:
                cur = q.popleft()
                if cur == des:
                    return cur,fuel+((cnt-1)*2)+1

                for d in direct:
                    i = cur[0] + d[0]
                    j = cur[1] + d[1]
                    if 0 <= i < N and 0 <= j < N:
                        if (i,j) in visited or board[i][j]:
                            continue
                        else:
                            visited.add((i, j))
                            tmp.append((i,j))

            if tmp:
                q.extend(tmp)
            else:
                return -1
        else:
            return -1

def find_cus(taxi, fuel):
    q = collections.deque()
    q.append(taxi)
    visited = {taxi}
    flag = True
    cus_rvs = []
    while 1:
        fuel-=1
        if fuel!=-1:
            tmp = []
            while q:
                cur = q.popleft()
                if cur in customer:
                    flag = False
                    cus_rvs.append(cur)
                    continue

                if flag:
                    for d in direct:
                        i = cur[0] + d[0]
                        j = cur[1] + d[1]
                        if 0 <= i < N and 0 <= j < N:
                            if (i, j) in visited or board[i][j]:
                                continue
                            else:
                                visited.add((i,j))
                                tmp.append((i,j))

            if cus_rvs:
                new = (1000,1000)
                for i in cus_rvs:
                    if i[0] < new[0]:
                        new = i[:]
                    elif i[0] == new[0] and i[1] < new[1]:
                        new = i[:]

                res = (new,customer[new],fuel+1)
                del(customer[new])
                return res

            elif tmp:
                q.extend(tmp)
            else:
                return -1
        else:
            return -1

N,M,fuel = map(int,input().split())
board = [list(map(int,input().split())) for _ in range(N)]
taxi = tuple(map(int,input().split()))
taxi = (taxi[0]-1,taxi[1]-1)
customer = {}
for i in range(1,M+1):
    a,b,c,d = map(int,input().split())
    customer[(a-1,b-1)] = (c-1,d-1)
di = [-1,0,1,0]
dj = [0,1,0,-1]
direct = [d for d in zip(di,dj)]
while customer:
    result = find_cus(taxi,fuel)
    if result==-1:
        break
    else:
        taxi, des, fuel = result

    result = find_des(taxi,des,fuel)
    if result == -1:
        break
    else:
        taxi, fuel = result


if result ==-1:
    print(-1)
else:
    print(fuel)