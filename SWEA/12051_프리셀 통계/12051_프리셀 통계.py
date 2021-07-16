import sys
sys.stdin = open('input.txt')

def eu(a,b):
    if a<b:
        a,b = b,a

    while b!=0:
        a = a%b
        a,b = b,a

    return a

T = int(input())
for t in range(1,T+1):
    N, Pd, Pg = map(int, input().split())
    res = 'Possible'

    tmp = eu(100,Pd)
    a = int(100 / tmp)
    b = int(Pd / tmp)

    if N < a or (Pd and Pg == 0):
        res = 'Broken'
    else:
        dif = a-b
        if (a-b and Pg == 100) or (a-b == 0 and Pg == 0):
            res = 'Broken'
        else:
            res = 'Possible'

    # print(tmp,a,b,Pg)
    print('#{} {}'.format(t,res))

