import sys
sys.stdin = open('input.txt')

N = int(input())
nums = [input() for _ in range(N)]
K = int(input())

dex = {}
dex2 = {}
alp = ['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']
for i in range(10):
    dex[str(i)] = i
    dex2[i] = str(i)
for i in range(len(alp)):
    dex[alp[i]] = i+10
    dex2[i+10] = alp[i]

sel = {}
for i in dex:
    sel[i] = []

tot = 0
for i in nums:
    k = 1
    q = 0
    for j in i[::-1]:
        tot += dex[j] * k
        k*=36

        sel[j].append(q)
        q+=1

data = []
for i in sel:
    if sel[i]:
        tmp = [i]
        x = 0
        for j in sel[i]:
            x += (35-dex[i])*(36**j)
        tmp.append(x)
        data.append(tmp)

new_data = sorted(data, key = lambda d : d[1],reverse=True)
new_tot = tot
for i in range(K):
    if len(new_data)-1 < i:
        break
    new_tot += new_data[i][1]

result = []
if not new_tot:
    result.append('0')

while new_tot:
    result.append(dex2[new_tot%36])
    new_tot//=36

print(''.join(result[::-1]))


