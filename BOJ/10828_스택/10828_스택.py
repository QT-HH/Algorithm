import sys
sys.stdin = open('input.txt')

N = int(sys.stdin.readline().strip())
stack = []
for _ in range(N):
    ctr = sys.stdin.readline().strip().split()
    if ctr[0] == 'push':
        stack.append(ctr[1])
    elif ctr[0] == 'pop':
        if stack:
            print(stack.pop())
        else:
            print(-1)
    elif ctr[0] == 'size':
        print(len(stack))
    elif ctr[0] == 'empty':
        if stack:
            print(0)
        else:
            print(1)
    elif ctr[0] == 'top':
        if stack:
            print(stack[-1])
        else:
            print(-1)
