import sys
sys.stdin=open('input.txt')

def find_cube(i,j):
    a,b = 0, 0
    for y in range(1,5):
        for x in range(1,y):
            if not board[i+x][j+y]:
                b = y-1
            for z in range()



board = [list(map(int,input().split())) for _ in range(10)]
papers = [0,5,5,5,5,5]
res = [25]
for i in range(10):
    for j in range(10):
            if board[i][j]:
                print(find_cube(i,j))
                break
    else:
        continue
    break