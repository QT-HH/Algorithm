import sys
sys.stdin = open('input.txt')
cup = [1,0,0]

def change(a):
    if a == 'A':
        cup[0],cup[1] = cup[1],cup[0]
    elif a == 'B':
        cup[1],cup[2] = cup[2],cup[1]
    elif a == 'C':
        cup[0],cup[2] = cup[2],cup[0]

history = list(input())
for h in history:
    change(h)

print(cup.index(1)+1)