import sys
sys.stdin = open('input.txt')

test = int(input())
for t in range(1,test+1):
    N = int(input())
    score = list(map(int,input().split()))
    case_max = sum(score)+1
    case = [0]*case_max
    case[0]=1
    for i in score:
        for j in range(case_max-1,-1,-1):
            if case[j]:
                case[j+i] = 1

    print(f'#{t} {sum(case)}')