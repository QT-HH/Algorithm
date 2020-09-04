import sys
sys.stdin = open('input.txt')

operator = {'+':1,'*':2,'(':0,')':3}
num = {'1','2','3','4','5','6','7','8','9','0'}
bracket = {'(':[],')':[]}

for t in range(1,11):
    N = int(input())
    eq = input()
    stack_opt = []
    stack = []
    for i in range(N):
        if eq[i] in operator:
            if eq[i] == '(':
                stack_opt.append(eq[i])
            elif eq[i] == ')':
                while stack_opt[-1] != '(':
                    stack.append(stack_opt.pop())
                stack_opt.pop()
            elif operator[eq[i]] < operator[stack_opt[-1]]:
                while operator[eq[i]] < operator[stack_opt[-1]]:
                    stack.append(stack_opt.pop())
                stack_opt.append(eq[i])
            else:
                stack_opt.append(eq[i])
        else:
            stack.append(eq[i])

    # print(eq)
    # print(''.join(stack))

    stack_cal=[]
    for i in stack:
        if i in num:
            stack_cal.append(i)
        elif i in operator:
            a = int(stack_cal.pop())
            b = int(stack_cal.pop())
            if i == '+':
                stack_cal.append(a+b)
            elif i == '*':
                stack_cal.append(a*b)

    print(f'#{t} {stack_cal[0]}')
