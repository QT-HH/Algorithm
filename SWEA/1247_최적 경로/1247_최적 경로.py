import sys
sys.stdin = open('input.txt')

def dfs(now,idx,tmp,cnt):
    if cnt >= result[0]:
        return

    if idx == N:
        node_l = abs(house[0]-tmp[-1][0]) + abs(house[1]-tmp[-1][1])
        result[0] = min(result[0],cnt + node_l)
    else:
        for i in range(N):
            if cust[i] not in tmp:
                tmp.append(cust[i])
                dfs(cust[i],idx+1,tmp,cnt + abs(now[0]-cust[i][0]) + abs(now[1]-cust[i][1]))
                tmp.pop()

T = int(input())
for t in range(1,T+1):
    N = int(input())
    homes = list(map(int,input().split()))
    comp = [homes[0],homes[1]]
    house = [homes[2],homes[3]]
    cust = []
    result = [9999999]
    tmp = []
    for i in range(4,len(homes),2):
        cust.append([homes[i],homes[i+1]])

    dfs(comp,0,tmp,0)

    print('#{} {}'.format(t,result[0]))