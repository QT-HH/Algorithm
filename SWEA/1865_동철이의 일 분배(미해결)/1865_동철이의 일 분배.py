import sys
sys.stdin = open('input.txt')

def btk(data):




test = int(input())
N = int(input())
data = [list(map(int,input().split())) for _ in range(N)]

result = [1]
for i in range(N):
    result[0] *= (data[i][i]/100)

