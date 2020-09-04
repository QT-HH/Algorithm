import sys
sys.stdin = open('input.txt')

def check(N,papers):
    result = 0
    if N < 0:
        return 0
    elif N == 0:
        return 1

    for i in papers:
        result += check(N-i,papers)
    return result



test = int(input())
for t in range(1,test+1):
    N = int(input())
    papers = [10,20,20]
    print(f'#{t} {check(N,papers)}')