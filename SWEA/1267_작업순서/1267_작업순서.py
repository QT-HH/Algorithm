import sys
sys.stdin = open('input.txt')

def line(i):
    if i in visited:
        return
    elif work.get(i):
        for j in work[i]:
            line(j)
        else:
            visited.append(i)
    else:
        visited.append(i)

for t in range(1,11):
    V,E = map(int,input().split())
    data = input().split()
    work = {}
    for i in range(0,len(data),2):
        if work.get(data[i+1]):
            work[data[i+1]].append(data[i])
        else:
            work[data[i+1]] = [data[i]]
    visited = list()
    for i in work:
        line(i)
    for i in range(1,V+1):
        if str(i) not in visited:
            visited.append(str(i))

    print(f'#{t} {" ".join(visited)}')
