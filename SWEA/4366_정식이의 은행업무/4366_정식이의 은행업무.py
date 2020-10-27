import sys
sys.stdin = open('input.txt')

T = int(input())
for t in range(1,T+1):
    two = input()
    thr = input()

    r_two = 0
    k = 1
    for i in two[::-1]:
        r_two += int(i)*k
        k<<=1

    r_thr = 0
    k = 1
    for i in thr[::-1]:
        r_thr += int(i)*k
        k*=3

    twos = []
    thrs = []

    k = 1
    for i in two[::-1]:
        i = int(i)
        if i:
            twos.append(r_two-k)
        else:
            twos.append(r_two+k)
        k<<=1

    k = 1
    for i in thr[::-1]:
        i = int(i)
        if i == 2:
            thrs.append(r_thr-k)
            thrs.append(r_thr-k*2)
        elif i == 1:
            thrs.append(r_thr-k)
            thrs.append(r_thr+k)
        else:
            thrs.append(r_thr+k)
            thrs.append(r_thr+k*2)
        k*=3

    for i in twos:
        for j in thrs:
            if i==j:
                result = i
                break
        else:
            continue
        break

    print('#{} {}'.format(t,result))
