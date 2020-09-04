import sys
sys.stdin = open('input.txt')

def btk(spot,stack,r):

    tmp_stack = stack[:]
    remain = set(r)
    remain.remove(spot)

    if tmp_stack and data[tmp_stack[-1]][spot] == 0:
        return
    else:
        tmp_stack.append(spot)
        # if tuple(set(tmp_stack)) in visited:
        #     return
        if len(tmp_stack) == N and data[spot][tmp_stack[0]]:
            total = 0
            for i in range(-1, N - 1):
                total += data[tmp_stack[i]][tmp_stack[i + 1]]
            if min_cost[0] > total:
                min_cost[0] = total
            return
        else:
            for i in remain:
                btk(i,tmp_stack,remain)
    return

import time
start = time.time()
N = int(input())
data = [list(map(int,input().split())) for _ in range(N)]
min_cost = [1000001*100]
visited = set()
btk(0,[],set(range(N)))
print(min_cost[0])
print(time.time()-start)