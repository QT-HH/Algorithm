import sys
sys.stdin = open('input.txt')

for t in range(1,11):
    cnt = int(input())
    boxes = list(map(int,input().split()))

    for i in range(cnt):
        x = boxes.index(max(boxes))
        y = boxes.index(min(boxes))

        boxes[x] -=1
        boxes[y] +=1

    max_val = max(boxes)
    min_val = min(boxes)

    print('#{} {}'.format(t,max_val-min_val))

