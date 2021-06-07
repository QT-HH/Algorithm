import sys
sys.stdin = open('input.txt')

N,M,X = map(int,sys.stdin.readline().rstrip().split())
board = [[101]*N for _ in range(N)]

for _ in range(M):
    i,j,T = map(int,sys.stdin.readline().rstrip().split())
    board[i-1][j-1] = T

rev_board = [i for i in zip(*board)]

result = board[X-1][:]
result[X-1] = 0
done = {X-1}

while len(done) < N:
    min_w = 101
    min_idx = -1
    for i in range(N):
        if i not in done and result[i] < min_w:
            min_w = result[i]
            min_idx = i

    done.add(min_idx)
    for i in range(N):
        if i not in done:
            tmp = min_w + board[min_idx][i]
            if result[i] > tmp:
                result[i] = tmp

rev_result = list(rev_board[X-1][:])
rev_result[X-1] = 0
rev_done = {X-1}

while len(rev_done) < N:
    min_w = 101
    min_idx = -1
    for i in range(N):
        if i not in rev_done and rev_result[i] < min_w:
            min_w = rev_result[i]
            min_idx = i

    rev_done.add(min_idx)
    for i in range(N):
        if i not in rev_done:
            tmp = min_w + rev_board[min_idx][i]
            if rev_result[i] > tmp:
                rev_result[i] = tmp

res = 0
for i in range(N):
    tmp = result[i]+rev_result[i]
    res = max(res, tmp)

print(res)
