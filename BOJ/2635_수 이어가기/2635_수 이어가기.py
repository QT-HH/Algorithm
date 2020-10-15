import sys
sys.stdin=open('input.txt')

N = int(input())
max_l = -1
max_li = []
for i in range(N//2,N+1):
    tmp = [N,i]
    while 1:
        res = tmp[-2]-tmp[-1]
        if res<0:
            if len(tmp)>max_l:
                max_l = len(tmp)
                max_li = tmp
            break
        else:
            tmp.append(res)

print(max_l)
print(*max_li)
