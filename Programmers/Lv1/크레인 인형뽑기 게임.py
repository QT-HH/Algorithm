def solution(board, moves):
    stack = []
    cnt = 0
    for i in moves:
        i -= 1
        for j in range(len(board)):
            if board[j][i]:
                if stack and stack[-1] == board[j][i]:
                    stack.pop()
                    cnt += 2
                else:
                    stack.append(board[j][i])

                board[j][i] = 0
                break

    answer = cnt
    return answer