import sys
sys.stdin = open('input.txt')

test = int(input())
for t in range(1,test+1):
    N = int(input())
    data = list(map(int,input().split()))
    case = [0]*(sum(data)+1)
    case[0] = 1
    for i in data:
        for j in range(len(case)-1,-1,-1):
            if case[j]:
                case[j+i] = 1

    print(f'#{t} {sum(case)}')
