import sys
sys.stdin = open('input.txt')

B,C,D = map(int,input().split())
A1,A2 = map(int,input().split())
E1,E2 = map(int,input().split())

l_b = int(A1*B/A2) + 1
if B*E1 == E2:
    r_b = int(B*E1/E2) - 1
else:
    r_b = int(B*E1/E2)




