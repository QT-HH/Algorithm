import sys
sys.stdin = open('input.txt')

check = {'(':')',')':'('}
N = int(sys.stdin.readline().strip())
for _ in range(N):
    stack = []
    now = sys.stdin.readline().strip()
    for i in range(len(now)):
        if not stack or now[i] == '(':
            stack.append(now[i])
        else:
            if stack[-1] == '(':
                stack.pop()
            else:
                stack.append(now[i])

    if stack:
        print('NO')
    else:
        print('YES')
