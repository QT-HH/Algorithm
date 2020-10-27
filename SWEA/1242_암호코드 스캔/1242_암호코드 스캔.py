import sys
sys.stdin = open('input.txt')

password = {
    (2,1,1):0,
    (2,2,1):1,
    (1,2,2):2,
    (4,1,1):3,
    (1,3,2):4,
    (2,3,1):5,
    (1,1,4):6,
    (3,1,2):7,
    (2,1,3):8,
    (1,1,2):9,
}

def add_check(result):
    if tuple(result) in total_visited:
        return 0

    tot = 0
    for i in range(len(result)-1):
        if i%2:
           tot+=result[i]
        else:
            tot+=result[i]*3
    else:
        tot+=result[-1]

    if tot%10:
        return 0
    else:
        total_visited.add(tuple(result))
        return sum(result)

def add_res(c1,c2,c3):
    check = min(c1, c2, c3)
    c1 //= check
    c2 //= check
    c3 //= check
    result.append(password[(c1, c2, c3)])
    return


T = int(input())

for t in range(1,T+1):
    N,M = map(int,input().split())
    code = [tuple(input().split()) for _ in range(N)]
    total = 0
    total_visited = set()
    visited = set()
    for i in code:
        if i in visited:
            continue
        else:
            visited.add(i)

        result = []
        c = bin(int(i[0],16)).lstrip('0').rstrip('0')
        if c != 'b':
            c1 = c2 = c3 = 0
            cc = 0
            for i in range(1,len(c)):
                if c[i] != c[i-1]:
                    cc += 1
                    if c[i] == 0 and c1 == 0:
                        cc = 0

                if c[i] == '1':
                    if cc == 1:
                        c1 += 1
                    else:
                        c3 += 1
                else:
                    if cc == 2:
                        c2 += 1
                    elif cc == 4:
                        add_res(c1, c2, c3)
                        c1 = c2 = c3 = 0
                        cc = 0
                if len(result) == 8:
                    total += add_check(result)
                    result = []
            else:
                add_res(c1, c2, c3)
                total += add_check(result)

    print('#{} {}'.format(t,total))
