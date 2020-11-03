import sys
sys.stdin = open('input.txt')

def bis(x,l,r,TF):
    c = (l+r)//2
    if l>r:
        return
    elif x == A[c]:
        result[0] += 1
    elif x < A[c] and (TF == False or TF == -1):
        bis(x, l, c-1, True)
    elif x > A[c] and (TF == True or TF == -1):
        bis(x, c+1, r, False)

T = int(input())
for t in range(1,T+1):
    N,M = map(int,input().split())
    A = sorted(list(map(int,input().split())))
    B = list(map(int,input().split()))
    result = [0]
    for b in B:
        bis(b,0,len(A)-1,-1)

    print('#{} {}'.format(t,result[0]))
