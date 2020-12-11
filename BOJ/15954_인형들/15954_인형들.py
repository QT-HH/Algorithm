import sys
sys.stdin = open('input.txt')

from decimal import Decimal
N,K = map(int,input().split())
dolls = [*map(int,input().split())]
dolls_sq = [*map(lambda x: x**2,dolls)]

for i in range(1,N):
    dolls[i] += dolls[i-1]
    dolls_sq[i] += dolls_sq[i-1]

dolls.append(0)
dolls_sq.append(0)

m_sq = (Decimal(dolls[N-1]) / Decimal(N)) ** 2
res = float((dolls_sq[N-1] - (m_sq * N)) / N) ** 0.5

for j in range(K,N):
    for i in range(j-1,N):
        m_sq = (Decimal(dolls[i]-dolls[i-j]) / Decimal(j)) ** 2
        tmp = float(((dolls_sq[i]-dolls_sq[i-j]) - (m_sq * j)) / j) ** 0.5
        res = min(res,tmp)

print(res)

