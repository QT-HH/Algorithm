import sys
sys.stdin = open('inpurt.txt')

def baby(p):
    ca = [0]*10
    for i in p:
        ca[i] += 1

    c = 0
    for i in ca:
        if i >= 3:
            return True

        if i:
            c += 1
        else:
            c = 0

        if c >= 3:
            return True

    return False

T = int(input())
for t in range(1,T+1):
    cards = list(map(int,input().split()))

    p1 = []
    p2 = []
    result = 0
    for i in range(len(cards)):
        if i%2:
            p2.append(cards[i])
        else:
            p1.append(cards[i])

        if baby(p1):
            result = 1
            break
        elif baby(p2):
            result = 2
            break

    print('#{} {}'.format(t,result))
