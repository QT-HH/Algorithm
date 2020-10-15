import sys
sys.stdin = open('inpurt.txt')

N = int(input())
ips = [list(map(int,input().split('.'))) for _ in range(N)]
netMask = [255]*4
netMask_min = [255]*4
netMask_max = [0]*4

for i in range(N):
    for j in range(4):
        netMask_min[j]&=ips[i][j]
        netMask_max[j]|=ips[i][j]

ip_min = netMask_min[:]

for i in range(4):
    if netMask_min[i] != netMask_max[i]:
        bench = (i,netMask_min[i],netMask_max[i])
        break
else:
    bench = (3,0,0)

cnt = 0
for i in range(9):
    if bench[1]>>i == bench[2]>>i:
        m = cnt
        break
    cnt+=1
else:
    m = 0


for i in range(3,-1,-1):
    if bench[0] == i:
        netMask[i]>>=m
        netMask[i]<<=m
        ip_min[i]>>=m
        ip_min[i]<<=m
        for j in range(3,i,-1):
            netMask[j] = 0
            ip_min[j] = 0
        break

print('.'.join(list(map(str,ip_min))))
print('.'.join(list(map(str,netMask))))