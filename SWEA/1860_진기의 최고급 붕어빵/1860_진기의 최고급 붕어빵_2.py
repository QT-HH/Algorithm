import sys
sys.stdin = open('input.txt')

T = int(input())

for tc in range(1, T+1):
    N, M, K = map(int,input().split())
    # N: 사람, M: 시간(초), K: 붕어빵
    customer = list(map(int,input().split()))
    customer.sort()

    bread = 0
    for t in range(1, max(customer)+1):
        if (t % M) == 0:
            bread += K
        for c in range(N):
            if customer[c] == t and bread != 0:
                bread -= 1
            elif customer[c] == t and bread == 0:
                result = "Impossible"
                break
            else:
                result = "Possible"

    print(result)