import sys
sys.stdin = open('input.txt')

def f1(n):
    global ans
    if n>=0:
        if n==99:
            ans=1
        f1(ch1[n])
        f1(ch2[n])

for t in range(1,11):
    tc, E = map(int,input().split())
    tmp = list(map(int,input().split()))
    ch1 = [-1]*100
    ch2 = [-1]*100
    for i in range(E):
        n1 = tmp[2*i]
        n2 = tmp[2*i+1]
        if ch1[n1]==-1:
            ch1[n1]=n2
        else:
            ch2[n1]=n2
    ans=0
    f1(0)
    print(ans)

