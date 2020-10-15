def solution(n):
    board = [[0] * n for _ in range(n)]
    cnt = [1]

    def put(starti, startj, down, right, up):
        cnt_tmp = cnt[0]
        for a in range(starti, down):
            if board[a][startj]:
                return
            else:
                board[a][startj] = cnt[0]
                cnt[0] += 1

        for a in range(startj+1, right):
            if board[down-1][a]:
                return
            else:
                board[down-1][a] = cnt[0]
                cnt[0] += 1

        for a in range(down - 2, up, -1):
            if board[a][right-1]:
                return
            else:
                board[a][right-1] = cnt[0]
                cnt[0] += 1

        if cnt_tmp == cnt[0]:
            return
        else:
            put(starti + 2, startj + 1, down - 1, right - 2, up + 2)

    put(0, 0, n, n, 0)
    answer = []
    for i in range(n):
        for j in range(n):
            if board[i][j]:
                answer.append(board[i][j])
    return answer

print(solution(4))
print(solution(5))
print(solution(6))