import sys
sys.stdin = open('input.txt')

def bfs():
    q = [board]
    print(q)
    cnt = 0
    while q:
        cnt+=1
        tmp = []
        for i in q:
            for j in range(9):
                tmp_li = list(i)
                for d in direct:
                    x = j+d
                    if 0<= x <9:
                        if tmp_li[x] == '*':
                            tmp_li[x] = '.'
                        else:
                            tmp_li[x] = '*'
                if tmp_li == result:
                    return cnt
                else:
                    tmp.append(tuple(tmp_li))

        q = tmp

direct = [0,-3,1,3,-1]
result = ['.']*9
P = int(input())
for t in range(P):
    board = [tuple(sys.stdin.readline().rstrip())  for _ in range(3)]

    print(board)
    # print(bfs())

