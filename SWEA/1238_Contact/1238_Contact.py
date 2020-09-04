import sys
sys.stdin = open('input.txt')

def find():
    q = [start]
    visited = set()
    while 1:
        tmp = []
        for i in q:
            if contact.get(i)==None:
                continue
            for j in contact[i]:
                if j in visited:
                    continue
                else:
                    visited.add(j)
                    tmp.append(j)
        if tmp:
            q = tmp
        else:
            return max(q)

for t in range(1,11):
    length, start = map(int,input().split())
    data = list(map(int,input().split()))
    contact = {}
    for i in range(0,length,2):
        if contact.get(data[i]):
            if data[i+1] in contact[data[i]]:
                continue
            else:
                contact[data[i]].append(data[i+1])
        else:
            contact[data[i]] = [data[i+1]]
    print(f'#{t} {find()}')