import sys
sys.stdin = open('input.txt')

def find():
    pass

T = int(input())
for t in range(1,T+1):
    num,cnt = input().split()
    num = tuple(num)
    cnt = int(cnt)

    visited = {num}
    while cnt:
        tmp_vis = set()
        for n in visited:
            for i in range(len(n)):
                for j in range(i+1,len(n)):
                    tmp = list(n)
                    tmp[i],tmp[j] = tmp[j], tmp[i]
                    if cnt>1:
                        tmp_vis.add(tuple(tmp))
                    else:
                        tmp_vis.add(int(''.join(tmp)))

        visited = tmp_vis
        cnt-=1

    print('#{} {}'.format(t,max(visited)))
