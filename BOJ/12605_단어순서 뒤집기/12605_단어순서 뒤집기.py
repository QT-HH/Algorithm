import sys
sys.stdin = open('input.txt')

N = int(input())
for t in range(1,N+1):
    sentence = input().split()[::-1]
    print('Case #{}: '.format(t)+' '.join(sentence))
