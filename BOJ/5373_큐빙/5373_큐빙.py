import sys
sys.stdin = open('input.txt')

def UD(i):
    # print('UD')
    if i[0] == 'U':
        a = 0
    else:
        a = 2
    if i[1] == '+':
        cube[i[0]] = [ list(x[::-1]) for x in zip(*cube[i[0]])]
    else:
        cube[i[0]] = [ list(x) for x in zip(*cube[i[0]])][::-1]

    if i == 'U+' or i == 'D-':
        x = 1
    else:
        x = 3

    b = 'FRBL'
    for k in range(x):
        for j in range(3):
            tmp = cube[b[0]][a][j]
            cube[b[0]][a][j] = cube[b[1]][a][j]
            cube[b[1]][a][j] = cube[b[2]][a][j]
            cube[b[2]][a][j] = cube[b[3]][a][j]
            cube[b[3]][a][j] = tmp


def LR(i):
    # print('LR')
    if i[0] == 'L':
        a = 0
    else:
        a = 2
    if i[1] == '+':
        cube[i[0]] = [ list(x[::-1]) for x in zip(*cube[i[0]])]
    else:
        cube[i[0]] = [ list(x) for x in zip(*cube[i[0]])][::-1]

    if i == 'L+' or i == 'R-':
        x = 1
    else:
        x = 3

    b = 'FUBD'
    for k in range(x):
        for j in range(3):
            tmp = cube[b[0]][j][a]
            cube[b[0]][j][a] = cube[b[1]][j][a]
            cube[b[1]][j][a] = cube[b[2]][2-j][2-a]
            cube[b[2]][2-j][2-a] = cube[b[3]][j][a]
            cube[b[3]][j][a] = tmp


def FB(i):
    # print('FB')
    if i[0] == 'F':
        a = 0
    else:
        a = 2
    if i[1] == '+':
        cube[i[0]] = [ list(x[::-1]) for x in zip(*cube[i[0]])]
    else:
        cube[i[0]] = [ list(x) for x in zip(*cube[i[0]])][::-1]

    if i == 'F+' or i == 'B-':
        x = 1
    else:
        x = 3

    b = 'ULDR'
    for k in range(x):
        for j in range(3):
            tmp = cube[b[0]][2-a][j]
            cube[b[0]][2-a][j] = cube[b[1]][2-j][2-a]
            cube[b[1]][2-j][2-a] = cube[b[2]][a][2-j]
            cube[b[2]][a][2-j] = cube[b[3]][j][a]
            cube[b[3]][j][a] = tmp




T = int(input())
for t in range(T):
    n = int(input())
    cube = {
        'U': [['w'] * 3 for _ in range(3)],
        'D': [['y'] * 3 for _ in range(3)],
        'F': [['r'] * 3 for _ in range(3)],
        'B': [['o'] * 3 for _ in range(3)],
        'L': [['g'] * 3 for _ in range(3)],
        'R': [['b'] * 3 for _ in range(3)]
    }

    turn = list(input().split())
    for i in turn:
        if i[0] in 'UD':
            UD(i)
        elif i[0] in 'LR':
            LR(i)
        else:
            FB(i)

    for i in cube['U']:
        print(''.join(i))