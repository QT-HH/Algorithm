import sys
sys.stdin = open('input.txt')

def check():
    cnt = 0
    for i in range(5):
        cnt_r = 0
        cnt_c = 0
        cnt_d = 0
        for j in range(5):
            if visit[i][j] == 1: # 가로
                cnt_r += 1
                if cnt_r == 5:
                    cnt += 1
            if visit[j][i] == 1: # 세로
                cnt_c += 1
                if cnt_c == 5:
                    cnt += 1
        if visit[i][i] == 1: # 왼쪽 대각선
            cnt_d += 1
            if cnt_d == 5:
                cnt += 1
        if visit[i][4-i] == 1: # 오른쪽 대각선
            cnt_d += 1
            if cnt_d == 5:
                cnt += 1
        if cnt >= 3:
            return (cnt_r + cnt_c + cnt_d)

bingo = [list(map(int, input().split())) for _ in range(5)]
visit = [[0]*5 for _ in range(5)]
count = []
for i in range(5):
    count += map(int, input().split())

for i in range(25):
    for r in range(5):
        for c in range(5):
            if count[i] == bingo[r][c]:
                visit[r][c] = 1

result = check()
print(result)
