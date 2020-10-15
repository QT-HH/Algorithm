import sys
sys.stdin = open('input.txt')

def find():
    for i in height:
        for j in height:
            if i == j:
                continue
            elif total - i - j == 100:
                height.remove(i)
                height.remove(j)
                return

height = sorted([int(input()) for _ in range(9)])
total = sum(height)
find()
for i in height:
    print(i)