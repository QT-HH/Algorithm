import sys
sys.stdin = open('input.txt')

opt = {'+','-','*','/'}
test = int(input())
for t in range(1,test+1):
    stack = []
    forth = list(input().split())
    for i in forth:
        if i in opt:
            if len(stack)<2 or stack[-1] in opt or stack[-2] in opt:
                stack = ['error']
                break
            b = stack.pop()
            a = stack.pop()
            if i == '+':
                stack.append(a+b)
            elif i == '-':
                stack.append(a-b)
            elif i == '*':
                stack.append(a*b)
            elif i == '/':
                if b == 0:
                    stack = ['error']
                    break
                else:
                    stack.append(a//b)
        elif i == '.':
            break
        else:
            stack.append(int(i))
    if len(stack) ==1:
        print(f'#{t} {stack[0]}')
    else:
        print(f'#{t} error')
