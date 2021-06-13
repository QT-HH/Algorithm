import sys
sys.stdin = open('input.txt')

input = sys.stdin.readline
N = int(input().rstrip())

for _ in range(N):
    commands = input().rstrip()
    stack1 = []
    stack2 = []
    for command in commands:
        if command == '<':
            if stack1: stack2.append(stack1.pop())
        elif command == '>':
            if stack2: stack1.append(stack2.pop())
        elif command == '-':
            if stack1: stack1.pop()
        else:
            stack1.append(command)

    print(''.join(stack1 + [*reversed(stack2)]))