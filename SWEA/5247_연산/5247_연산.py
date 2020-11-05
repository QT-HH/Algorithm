import sys
sys.stdin = open('input.txt')

T = int(input())
for t in range(1,T+1):
    N,M = map(int,input().split())

    q = [N]
    visited = set()
    cnt = -1
    while q:
        cnt+=1
        tmp = []
        for now in q:
            if now == M:
                break
            elif now > 1000000:
                continue
            elif now in visited:
                continue
            visited.add(now)
            tmp.append(now+1)
            tmp.append(now-1)
            tmp.append(now*2)
            tmp.append(now-10)
        else:
            q = tmp
            continue
        break

    print('#{} {}'.format(t,cnt))
