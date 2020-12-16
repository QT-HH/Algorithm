import sys
sys.stdin = open('input.txt')

T = int(sys.stdin.readline().rstrip())
for t in range(T):
    p = sys.stdin.readline().rstrip()
    n = int(sys.stdin.readline().rstrip())
    arr = sys.stdin.readline().rstrip().lstrip('[').rstrip(']').split(',')

    l,r = 0,n
    rev = 1
    res = True
    for i in p:
        if i == 'R':
            if l>=r:
                continue
            rev *= -1
        elif i == 'D':
            if l>=r:
                res = False
                break
            elif rev == 1:
                l += 1
            else:
                r -= 1

    if not res:
        print('error')
    elif arr == [''] or l==r:
        print([])
    elif rev == 1:
        print('[{}]'.format(','.join(arr[l:r])))
    elif l == 0:
        print('[{}]'.format(','.join(arr[r-1::-1])))
    else:
        print('[{}]'.format(','.join(arr[r-1:l-1:-1])))
