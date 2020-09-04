def pal(x):
    for i in range(1, 101)[::-1]:
        for words in x:
            for j in range(100 - i + 1):
                y = words[j:i+j]
                if y == y[::-1]:
                    return i

import sys
import time
sys.stdin = open('sample_input.txt')
for test_case in range(1, 11):
    start = time.time()
    n = int(input())
    board = [input() for i in range(100)]
    board_col = [''.join(i) for i in zip(*board)]
    row = pal(board)
    col = pal(board_col)
    result = max(row, col)

    print(f'#{n} {result}')
    print(time.time()-start)