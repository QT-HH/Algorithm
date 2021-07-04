import sys
sys.stdin = open('input.txt')
input = sys.stdin.readline

W, H, f, c, x1, y1, x2, y2 = map(int,input().rstrip().split())
res = W * H
if f > W-f:
    x1 += f
    x2 += f
    cell = (x2-x1) * (y2-y1)
    if x2 <= W:
        left_cell = cell
    elif x1 <= W < x2:
        left_cell = (W-x1) * (y2-y1)
    else:
        left_cell = 0
    res -= (cell + left_cell) * (c + 1)

else:
    x1 += f
    x2 += f
    lim = f+f
    cell = (x2-x1) * (y2-y1)
    if x2 <= lim:
        left_cell = cell
    elif x1<= lim <x2:
        left_cell = (lim-x1) * (y2-y1)
    else:
        left_cell = 0
    res -= (cell + left_cell) * (c + 1)

print(res)