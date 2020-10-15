import sys
sys.stdin = open('input.txt')

T = int(input())
for tc in range(T):
    N = int(input())
    scores = list(map(int, input().split()))
    result = set()
    result.add(0)
    tmp = set()
    for i in range(len(scores)):
        for j in result:
            tmp.add(j+scores[i])
        result.update(tmp)
    print(f'#{tc+1} {len(result)}')