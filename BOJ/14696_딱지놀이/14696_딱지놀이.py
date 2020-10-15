import sys
sys.stdin = open('input.txt')

N = int(input())
for _ in range(N):
    A = list(map(int,input().split()))
    B = list(map(int,input().split()))
    A_card = [0]*5
    B_card = [0]*5
    for a in range(1,A[0]+1):
        A_card[A[a]]+=1
    for b in range(1,B[0]+1):
        B_card[B[b]]+=1

    for i in range(4,0,-1):
        if A_card[i]<B_card[i]:
            print('B')
            break
        elif A_card[i]>B_card[i]:
            print('A')
            break
        else:
            if i==1:
                print('D')