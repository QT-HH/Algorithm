import sys
sys.stdin = open('input1.txt')

N = int(input()) # 100
max_l = -1
max_li = []
for i in range(1,N+1):
    tmp = [N,i] # 다음 숫자는 N-i
    while 1:
        next = tmp[-2]-tmp[-1]
        if next < 0:
            if len(tmp) > max_l:
                max_l = len(tmp)
                max_li = tmp
            break
        else:
            tmp.append(next)

print(max_l)
print(*max_li)