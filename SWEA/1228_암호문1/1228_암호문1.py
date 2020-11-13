import sys
sys.stdin = open('input.txt')

for t in range(1,11):
    N = int(input())
    password = list(map(int,input().split()))
    M = int(input())
    x = list(input().split('I'))
    y = []
    for i in x:
        if i:
            y.append(list(map(int,i.split())))

    for i in y:
        password = password[:int(i[0])] + i[2:] + password[int(i[0]):]

    print('#{} {} {} {} {} {} {} {} {} {} {}'.format(t, *password[:10]))
