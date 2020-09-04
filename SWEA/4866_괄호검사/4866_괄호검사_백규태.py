import sys
sys.stdin = open('input.txt')

close = [')','}']
start = ['(','{']
N=int(input())
for n in range(1,N+1):
    result = 0
    code = list(input())
    stack = []
    while code:
        x = code.pop()
        if x in close:
            stack.append(x)
        elif x in start:
            if stack == [] or start.index(x) != close.index(stack[-1]):
                break
            else:
                stack.pop()
    else:
        if stack==[]:
            result = 1

    print(f'#{n} {result}')
