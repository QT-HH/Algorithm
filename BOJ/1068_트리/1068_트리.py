import sys
sys.stdin = open('input.txt')

input = sys.stdin.readline
N = int(input().rstrip())
tree = [[] for _ in range(N)]
parent = [*map(int,input().rstrip().split())]
rm = int(input().rstrip())

exc = [rm]

for i,j in enumerate(parent):
    if j == -1:
        pass
    else:
        tree[j].append(i)

while exc:
    now = exc.pop()
    exc.extend(tree[now])
    tree[now] = [-2]

res = 0
# print(tree)
for i in tree:
    if not i or i == [rm]:
       res += 1

print(res)

