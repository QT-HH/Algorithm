import sys
sys.stdin = open('input.txt')

N = int(input())
tree = {}
for i in range(N-1):
    a,b = map(int,sys.stdin.readline().split())
    if tree.get(a):
        tree[a].add(b)
    else:
        tree[a] = {b}

order = list(map(int,input().split()))

if order[0] != 1:
    print(0)
else:
    stack = [1]
    i = 1
    while stack and i < N:
        if tree.get(stack[-1]) and order[i] in tree[stack[-1]]:
            stack.append(order[i])
            i += 1
        else:
            stack.pop()

    if not stack or i < N:
        print(0)
    else:
        print(1)

