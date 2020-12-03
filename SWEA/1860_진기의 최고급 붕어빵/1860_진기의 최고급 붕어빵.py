import sys
sys.stdin = open('input.txt')

T = int(input())
for t in range(1,T+1):
    N,M,K = map(int,input().split())
    son = list(map(int,input().split()))

    sons = {}
    for i in son:
        if sons.get(i):
            sons[i] += 1
        else:
            sons[i] = 1

    time = 0
    cnt = 0
    bread = 0
    i = 0

    if 0 in sons:
        result = 'Impossible'
    else:
        while i < N:
            time += 1
            cnt += 1
            if cnt == M:
                cnt = 0
                bread += K

            if sons.get(time):
                bread -= sons[time]
                i += sons[time]

            if bread < 0:
                result = 'Impossible'
                break

        else:
            result = 'Possible'

    print('#{} {}'.format(t,result))
