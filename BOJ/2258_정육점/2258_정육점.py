import sys
sys.stdin = open('input.txt')

N,M = map(int,input().split())
meats = {}
for i in range(N):
    a,b = map(int,sys.stdin.readline().split())
    if meats.get(b):
        meats[b][0] += a
        meats[b].append(a)
    else:
        meats[b] = [a,a]

meats_list = sorted(list(meats))
result = -1
total = 0
for i in range(len(meats_list)):
    total += meats[meats_list[i]][0]
    if total >= M:
        total -= meats[meats_list[i]][0]
        meats[meats_list[i]].sort(reverse=True)
        for j in range(1,len(meats[meats_list[i]])):
            total += meats[meats_list[i]][j]
            if total >= M:
                if i < len(meats_list)-1:
                    if meats_list[i]*j < meats_list[i+1]:
                        result = meats_list[i]*j
                        break
                    else:
                        result = meats_list[i+1]
                        break
                else:
                    result = meats_list[i]*j
                    break
    else:
        continue
    break

print(result)