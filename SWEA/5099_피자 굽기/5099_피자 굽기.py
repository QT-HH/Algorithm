import sys
sys.stdin = open('input.txt')

def pizza(stove):
    tmp = []
    while 1:
        for i in stove:
            if i[1]:
                i[1] //= 2
            elif len(dough):
                x = dough.popleft()
                x[1]//=2
                stove[stove.index(i)] = x
            else:
                tmp.append(i)
                stove[stove.index(i)] = [-1,-1]
                if len(tmp) == N-1:
                    for j in stove:
                        if j[1] >=0:
                            return j[0]+1

import collections
test = int(input())
for t in range(1,test+1):
    N,M = map(int,input().split())
    dough = collections.deque()
    dough.extend([list(x) for x in enumerate(list(map(int,input().split())))])
    stove = []
    for i in range(N):
        stove.append(dough.popleft())
    print(f'#{t} {pizza(stove)}')
