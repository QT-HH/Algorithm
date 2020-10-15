import sys
sys.stdin = open('input.txt')

n = int(input())
dices = []
for _ in range(n):
    a,b,c,d,e,f = map(int, input().split())
    dices.append([(a,f),(b,d),(c,e)])

res = 0
for i in range(3):
    for j in range(2):
        bot = dices[0][i][j]
        top = dices[0][i][j-1]
        if 6 in dices[0][i]:
            if 5 in dices[0][i]:
                total = 4
            else:
                total = 5
        else:
            total = 6

        for k in range(1,n):
            for l in range(3):
                if top in dices[k][l]:
                    if top == dices[k][l][0]:
                        bot = dices[k][l][0]
                        top = dices[k][l][1]
                    else:
                        bot = dices[k][l][1]
                        top = dices[k][l][0]

                    if 6 in dices[k][l]:
                        if 5 in dices[k][l]:
                            total+=4
                        else:
                            total+=5
                    else: total+=6

        if res<total:
            res = total

print(res)