import sys
sys.stdin = open('input.txt')

t = 0
while 1:
    t += 1
    res = -160000001
    data = list(map(int,input().split()))
    if data[0] == 0:
        break

    tri = []
    tmp = []
    acc = 0
    cnt = 0
    cnt_t = 1
    for i in range(1,len(data)):
        cnt+=1
        acc += data[i]
        tmp.append(acc)
        if cnt == cnt_t:
            tri.append(tmp) 
            tmp = []
            cnt_t += 2
            cnt = 0
            acc = 0



    print(tri)


    # print('{}. {}'.format(t,res))