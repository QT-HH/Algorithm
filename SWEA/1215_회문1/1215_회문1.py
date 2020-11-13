import sys
sys.stdin = open('input.txt')

for t in range(1,11):
    k = int(input())
    box = [input() for _ in range(8)]
    box_col = [''.join(x) for x in zip(*box)]

    cnt=0
    for i in range(8):
        for j in range(0,9-k):
            if box[i][j:j+k] == box[i][j:j+k][::-1]:
                cnt+=1
            if box_col[i][j:j+k] == box_col[i][j:j+k][::-1]:
                cnt+=1

    print('#{} {}'.format(t,cnt))

