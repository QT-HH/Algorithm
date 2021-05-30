import sys
sys.stdin = open('input.txt')

N, M = map(int,input().split())
r, c, d = map(int,input().split())
next_d = [3, 0, 1, 2]
back_d = [2, 3, 0, 1]

# 북 동 남 서
y = [-1, 0, 1, 0]
x = [0, 1, 0, -1]
direction = [di for di in zip(y,x)]

myRoom = [[*map(int,input().split())] for _ in range(N)]
t_cnt = 0
ans = 0

while True:
    if t_cnt != 4:
        if myRoom[r][c] == 0:
            myRoom[r][c] = 2
            ans += 1
        next_r, next_c = r, c

        cnt = 0
        next_r += direction[next_d[d]][0]
        next_c += direction[next_d[d]][1]
        d = next_d[d]
        if myRoom[next_r][next_c]:
            t_cnt += 1
        else:
            r = next_r
            c = next_c
            t_cnt = 0

    else:
        back_r = r + direction[back_d[d]][0]
        back_c = c + direction[back_d[d]][1]
        if myRoom[back_r][back_c] == 1:
            break
        else:
            r, c = back_r, back_c
            t_cnt = 0

    # print(r,c,d, t_cnt)

print(ans)

