import sys
sys.stdin = open('input.txt')

N,K = map(int,input().split())
st = {1:[0,0,0,0,0,0,0], 0:[0,0,0,0,0,0,0]}
for i in range(N):
    s,g = map(int,input().split())
    if s:
        st[1][g]+=1
    else:
        st[0][g]+=1

cnt = 0
for i in st:
    for j in st[i]:
        cnt+=j//K
        if j%K:
            cnt+=1

print(cnt)