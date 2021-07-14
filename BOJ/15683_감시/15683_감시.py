import sys
sys.stdin = open('input.txt')
input = sys.stdin.readline

def

N, M = map(int,input().rstrip().split())
room = [[*map(int,input().rstrip().split())] for _ in range(N)]
cameras = []
walls = set()
for i in range(N):
    for j in range(M):
        if 0 < room[i][j] <= 5:
            cameras.append((i, j, room[i][j]))
        elif room[i][j] == 6:
            walls.add((i,j))

for c in cameras:
    pass