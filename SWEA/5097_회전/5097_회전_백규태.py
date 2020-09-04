import sys
sys.stdin = open('input.txt')

import collections
test = int(input())
for t in range(1,test+1):
    N,M = map(int,input().split())
    M = M%N
    data = input().split()
    q = collections.deque()
    q.extend(data)
    for i in range(M):
        x = q.popleft()
        q.append(x)
    print(f'#{t} {q.popleft()}')