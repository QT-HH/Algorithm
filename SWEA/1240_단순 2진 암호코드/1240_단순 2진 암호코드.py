import sys
sys.stdin = open('input.txt')

password = {
    (0,0,0,1,1,0,1) : 0,
    (0,0,1,1,0,0,1) : 1,
    (0,0,1,0,0,1,1) : 2,
    (0,1,1,1,1,0,1) : 3,
    (0,1,0,0,0,1,1) : 4,
    (0,1,1,0,0,0,1) : 5,
    (0,1,0,1,1,1,1) : 6,
    (0,1,1,1,0,1,1) : 7,
    (0,1,1,0,1,1,1) : 8,
    (0,0,0,1,0,1,1) : 9,
}

def find(si,sj):
    res = []
    for i in range(0,56,7):
        tmp = []
        for j in range(7):
            tmp.append(int(code[si][sj+i+j]))
        if password.get(tuple(tmp))==None:
            return 0
        else:
            res.append(password[(tuple(tmp))])

    # print(res)
    if len(res)==8:
        tot = 0
        for i in range(len(res)-1):
            if i%2:
                tot += res[i]
            else:
                tot += res[i]*3

        tot+=res[-1]
        if tot%10:
            result = 0
        else:
            result = sum(res)
    else:
        result = 0

    return result

T = int(input())
for t in range(1,T+1):
    N,M = map(int,input().split())

    code = [input() for _ in range(N)]

    for i in range(N-1,-1,-1):
        for j in range(M-1,-1,-1):
            if code[i][j]=='1':
                si = i-4
                sj = j-55
                break
        else:
            continue
        break

    print(f'#{t} {find(si,sj)}')
