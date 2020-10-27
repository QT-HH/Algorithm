import sys
sys.stdin = open('input.txt')

hed = {}
for i in range(10):
    hed[str(i)]=i
tmp = ['A','B','C','D','E','F',]
for i in range(len(tmp)):
    hed[tmp[i]] = i+10

print(hed)

T = int(input())
for t in range(1,T+1):
    N,num = input().split()

    res = []
    for i in range(int(N)):
        x = hed[num[i]]
        r_res = []
        for j in range(4):
            r_res.append(str(x%2))
            x//=2
        res.append(''.join(r_res[::-1]))

    print('#{} {}'.format(t,''.join(res)))


