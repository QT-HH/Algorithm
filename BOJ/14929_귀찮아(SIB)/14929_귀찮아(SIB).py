import sys
sys.stdin = open('input.txt')

N = int(input())
x_list = list(map(int,input().split()))

result = 0
total = sum(x_list)
for i in x_list:
    total -= i
    result += i*(total)

print(result)