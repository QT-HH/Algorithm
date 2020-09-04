def change(x,i,M):
    a = x[i:i+M]
    b = x[:]
    b[i:i+M] = a[::-1]
    return b

def game(N,M,y,total,rv,cnt):
    while(y):
        for n in y:
            cnt+=1
            for i in range(N-M+1):
                temp = change(n,i,M)
                if tuple(temp) in total:
                    continue
                if temp == rv:
                    return cnt
                else:
                    y.append(temp)
                    total.add(tuple(temp))
            else:
                y.popleft()
    else: 
        return -1

from collections import deque
N,M = map(int,input().split())
x = list(map(int,input().split()))
rv = sorted(x)
y = deque()
y.append(x[:])
total = {tuple(x)}
cnt = 0

if x == rv:
    print(0)
else:
    print(game(N,M,y,total,rv,cnt))
