import sys
sys.stdin = open('input.txt')

r, c = map(int, input().split()) # 가로, 세로 크기
n = int(input()) # 자를 점선의 갯수
row = [0] # 가로 리스트
col = [0] # 세로 리스트
# print(paper)
for i in range(n):
    a, b = map(int, input().split())
    if a == 0: # a 가 0이라면 가로 리스트에 추가
        row.append(b)
    elif a == 1: # a 가 1 이라면 세로 리스트에 추가
        col.append(b)
row.sort() # 순서대로 정렬되어야 길이를 맞게 구할 수 있음
col.sort()
row.append(r) # 가로의 길이를 추가해 주어야 계산 가능
col.append(c) # 세로의 길이를 추가해 주어야 길이 계산 가능능
print(row)
print(col)
max_r = 0
for i in range(1, len(row)): #가로 길이에서의 최댓값 구하기
    a = row[i] - row[i-1]
    if max_r < a:
        max_r = a
max_c = 0
for i in range(1, len(col)): # 세로 길이에서의 최댓값 구하기
    a = col[i] - col[i-1]
    if max_c < a:
        max_c = a
print(max_r,max_c)
print(max_r*max_c)