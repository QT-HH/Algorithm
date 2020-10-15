import sys
sys.stdin = open('input.txt')

test = int(input())
for t in range(1,test+1):
    N,B = map(int,input().split())
    data = list(map(int,input().split()))
    X = sum(data)+1
    case = [0]*X
    case[0] = 1
    for j in data:
        for i in range(len(case)-1,-1,-1):
            if case[i]:
                case[i+j] = 1

    for i in range(B,X):
        if case[i]:
            print(f'#{t} {i-B}')
            break