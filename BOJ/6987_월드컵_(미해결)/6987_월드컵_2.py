import sys
sys.stdin = open('input.txt')

def judge(a,b,c,d,e,f):


result = []
data = [list(map(int,input().split())) for _ in range(4)]
for d in data:
    ranking = []
    for i in range(0,18,3):
        ranking.append(d[i:i+3])
