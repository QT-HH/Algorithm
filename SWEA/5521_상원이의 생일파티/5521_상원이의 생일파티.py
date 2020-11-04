import sys
sys.stdin = open('input.txt')

T = int(input())

for t in range(1,T+1):
    N,M = map(int,input().split())
    friends = {}
    for i in range(M):
        a,b = map(int,input().split())
        if friends.get(a):
            friends[a].append(b)
        else:
            friends[a] = [b]
        if friends.get(b):
            friends[b].append(a)
        else:
            friends[b] = [a]

    invited = {1}
    if friends.get(1):
        invited.update(friends[1])
        for i in friends[1]:
            if friends.get(i):
                invited.update(friends[i])

    print('#{} {}'.format(t,len(invited)-1))

