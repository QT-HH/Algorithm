import sys
sys.stdin = open('input.txt')

def compare(x,y):
    if y[1]-x[1] in (1,-2):
        return y
    else:
        return x

def game(cards):
    if len(cards) == 2:
        return compare(cards[0],cards[1])
    elif len(cards) == 1:
        return cards[0]
    else:
        center = (len(cards)+1)//2
        cards1 = cards[:center]
        cards2 = cards[center:]
        return compare(game(cards1),game(cards2))

test = int(input())
for t in range(1,test+1):
    N = int(input())
    cards = list(map(int,input().split()))
    cards_num = [[i+1,j] for i,j in enumerate(cards)]
    print(f'#{t} {game(cards_num)[0]}')
