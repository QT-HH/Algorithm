import sys
sys.stdin = open('input.txt')

dualList = [*map(lambda x: x*x, range(100000000000000))]

T = int(input())
for t in range(1,T+1):
    x = int(input())
    y = x**0.5
    if y == int(y):
        y=int(y)
    else:
        y=int(y)+1

    for i in range(y,3164):
        if not dualList[i]%x:
            res = dualList[i]//x
            break

    print('#{} {}'.format(t, res))
