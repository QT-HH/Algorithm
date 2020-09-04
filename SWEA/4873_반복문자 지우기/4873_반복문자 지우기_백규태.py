import sys
sys.stdin = open('input.txt')

test = int(input())
for t in range(1,test+1):
    words = input()
    stack = []
    for i in range(len(words)):
        stack.append(words[i])
        while 1:
            if len(stack)>1:
                if stack[-1] == stack[-2]:
                    stack.pop()
                    stack.pop()
                else:
                    break
            else:
                break
    print(f'#{t} {len(stack)}')