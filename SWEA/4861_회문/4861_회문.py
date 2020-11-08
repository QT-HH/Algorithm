import sys
sys.stdin = open('input.txt')

T = int(input())

for tc in range(1):
    N, M = map(int,input().split())
    arr = [list(map(str,input())) for _ in range(N)]

    for i in range(N-M+1):
        for j in range(N-M+1):
            new_arr = []
            for t in range(i,i+M):
                row_arr = []
                for b in range(j,j+M):
                    row_arr.append(arr[t][b])
                new_arr.append(new_arr)
