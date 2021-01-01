import sys
sys.stdin = open('input.txt')

N,L = map(int,sys.stdin.readline().split())
nodes = {}
for i in range(L):
    stations = list(map(int,sys.stdin.readline().split()))
    for j in range(len(stations)-1):
        if nodes.get(stations[j]):
            nodes[stations[j]].append(i)
        else:
            nodes[stations[j]] = [i]