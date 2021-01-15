import sys
sys.stdin = open('input.txt')

N = int(sys.stdin.readline().strip())
stack = []
for _ in range(N):
    x = int(sys.stdin.readline().strip())
    stack.append(x)

cnt = 0
last = stack[-1]
for i in range(N-2,-1,-1):
    if stack[i]>last:
        cnt+=1
        last = stack[i]

print(cnt+1)