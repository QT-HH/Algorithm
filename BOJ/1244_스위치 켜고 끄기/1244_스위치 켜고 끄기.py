import sys
sys.stdin = open('input.txt')

def ispal(x):
    for i in range(len(x)//2):
        if x[i]==x[-1-i]:
            continue
        else:
            return False
    return True

N = int(input())
switch = list(map(int,input().split()))
S = int(input())
change = [list(map(int,input().split())) for _ in range(S)]
for i in change:
    if i[0]==1:
        cnt=1
        while 1:
            t=i[1]*cnt
            if 0<=t-1<N:
                if switch[t-1]:
                    switch[t-1]=0
                else:
                    switch[t-1]=1
                cnt+=1
            else:
                break
    else:
        t = i[1]-1
        if t<=(N-1)//2:
            start = 0
            end = t*2+1
        else:
            start = t-(N-t)+1
            end = N
        while 1:
            if start == t:
                if switch[t]:
                    switch[t] = 0
                else:
                    switch[t] = 1
                break

            if ispal(switch[start:end]):
                for i in range(start,end):
                    if switch[i]:
                        switch[i]=0
                    else:
                        switch[i]=1
                break
            else:
                start+=1
                end-=1

start = 0
end = 20
while 1:
    print(*switch[start:end])
    if end < len(switch):
        start+=20
        end+=20
    else:
        break