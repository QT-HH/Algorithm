import sys
sys.stdin = open('input.txt')

def inord(value):
    if value:
        if len(table[value]) >=3:
            inord(int(table[value][2]))
        result.append(table[value][1])
        if len(table[value]) == 4:
            inord(int(table[value][3]))

for t in range(1,11):
    N = int(input())
    table = [[0,0,0,0]]
    for _ in range(N):
        table.append(input().split())
    result = []
    inord(1)
    print(f'#{t} {"".join(result)}')