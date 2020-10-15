import sys
sys.stdin = open('input.txt')

def find():
    cnt=0
    i,j = (R,0)
    while 1:
        for d in direct:
            while True:
                if 0<=i+d[0]<R and 0<=j+d[1]<C and not sit[i+d[0]][j+d[1]]:
                    i += d[0]
                    j += d[1]
                    cnt+=1
                    sit[i][j]=cnt
                    if cnt== num:
                        return j+1,R-i
                else:
                    break

di = [-1,0,1,0]
dj = [0,1,0,-1]
direct = [d for d in zip(di,dj)]

C,R = map(int,input().split())
num = int(input())

sit = [[0]*C for _ in range(R)]
if num > C*R:
    print(0)
else:
    print(*find())