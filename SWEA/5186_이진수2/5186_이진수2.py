import sys
sys.stdin = open('input.txt')

def two(num):
    n = -1
    res = []
    while n > -14:
        if num >= 2 ** n:
            res.append('1')
            num -= 2 ** n
            if not num:
                break
        else:
            res.append('0')

        n -= 1
    else:
        print(res)
        return 'overflow'

    return ''.join(res)


T = int(input())
for t in range(1,T+1):
    num = float(input())

    print('#{} {}'.format(t,two(num)))