import sys
sys.stdin = open('input.txt')

T = int(input())
for t in range(1,T+1):
    N,M,K = map(int,input().split())
    microbes = {}
    for i in range(K):
        a,b,c,d = map(int,input().split())
        microbes[(a,b)] = [[c,d]]
    direct = [0,(-1,0),(1,0),(0,-1),(0,1)]
    turn = {1:2, 2:1, 3:4, 4:3}
    # print(microbes)
    for time in range(M):
        tmp = {}
        for m in microbes:
            y = m[0]+direct[microbes[m][0][1]][0]
            x = m[1]+direct[microbes[m][0][1]][1]
            if y == 0 or y == N-1 or x == 0 or x == N-1:
                microbes[m][0][0]//=2
                microbes[m][0][1] = turn[microbes[m][0][1]]

            if tmp.get((y,x)):
                tmp[(y,x)].append(microbes[m][0])
            else:
                tmp[(y,x)] = microbes[m]

        for i in tmp:
            if len(tmp[i]) > 1:
                # print(tmp)
                tmp[i].sort(key=lambda x: x[0])
                for j in range(len(tmp[i])-1):
                    tmp[i][-1][0] += tmp[i][j][0]
                tmp[i] = [tmp[i][-1]]

        microbes = tmp

    total = 0
    # print(microbes)
    for i in microbes:
        total += microbes[i][0][0]

    print('#{} {}'.format(t,total))