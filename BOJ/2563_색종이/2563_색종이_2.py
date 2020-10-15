import sys
sys.stdin = open('input.txt')

N = int(input())
init = [[0]*100 for _ in range(100)]
for tmp in range(N):
    x1, y1 = map(int, input().split())
    x2, y2 = (x1+10), (y1+10)
    for i in range(x1, x2):
        for j in range(y1, y2):
            if init[j][i]==0:
                init[j][i]=1
            else:
                init[j][i]+=1

for i in range(x1, x2):
    for j in range(y1, y2):
        if init[j][i]!=0 and init[j][i]!=1:
          init[j][i]=1
        else:
            continue

cnt = 0
for k in range(len(init)):
    cnt += init[k].count(1)
print(cnt)
for i in init:
    print(i)