import sys
sys.stdin = open('input.txt')

T = int(input())
for test_case in range(1, T + 1):
    N,M = map(int, input().split())
    box = [input() for _ in range(N)]
    box_col = [''.join(i) for i in zip(*box)]
    result = ''
    for i in box:
        for j in range(len(i)-M+1):
            x = i[j:j+M]
            for k in range(M):
                if x[k]!=x[-1-k]:
                    break
            else:
                result+=x
    for i in box_col:
        for j in range(len(i)-M+1):
            x = i[j:j+M]
            for k in range(M):
                if x[k]!=x[-1-k]:
                    break
            else:
                result+=x
    print(f'#{test_case} {result}')