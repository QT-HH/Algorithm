import sys
sys.stdin = open('input.txt')

T = int(sys.stdin.readline())
for t in range(T):
    n = int(sys.stdin.readline())
    nums = sorted([sys.stdin.readline().rstrip() for _ in range(n)])
    for i in range(n-1):
        x = len(nums[i])
        if nums[i] == nums[i+1][:x]:
            print('NO')
            break
    else:
        print('YES')


