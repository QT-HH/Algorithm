import sys
sys.stdin = open('input.txt')

def find(a,b,c):
    # a = 현재 인덱스
    # b = 원본 길이
    # c = tmp
    tmp = c[:]
    if a == b-1:
        res.append(tuple(tmp))
        c.pop()
        return
    else:
        for i in range(a,b):
            tmp.append(sng[i])
            find(a+1,b,tmp)



N = int(input())
sng = [ list(map(int,input().split())) for _ in range(N) ]
res = []
n = N//2

find(0,len(sng),[])
print(res)



