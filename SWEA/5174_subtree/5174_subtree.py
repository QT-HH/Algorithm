import sys
sys.stdin = open('input.txt')

def find(value):
    global cnt
    if value:
        for i in table[value]:
            if i:
                cnt+=1
                find(i)

test = int(input())
for t in range(1,test+1):
    E,N = map(int,input().split())
    data = list(map(int,input().split()))
    table = [[0,0] for _ in range(E+2)]
    for i in range(0,len(data),2):
        if table[data[i]][0]:
            table[data[i]][1] = data[i+1]
        else:
            table[data[i]][0] = data[i+1]
    cnt=1
    find(N)
    print(f'#{t} {cnt}')