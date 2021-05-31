import sys
sys.stdin=open('input.txt')

N = int(sys.stdin.readline().rstrip())
graph = [set() for _ in range(N+1)]
visited = {1}

for _ in range(N-1):
    x,y = map(int,sys.stdin.readline().rstrip().split())
    graph[x].add(y)
    graph[y].add(x)

path = [*map(int,sys.stdin.readline().rstrip().split())]
stack = [1]
i = 1

while stack and i < N:
    if path[i] in graph[stack[-1]]:
        if path[i] in visited:
            stack = []
            break
        stack.append(path[i])
        visited.add(path[i])
        i+=1
    else:
        stack.pop()

if path[0] != 1:
    print(0)
elif not stack or i < N:
    print(0)
else:
    print(1)