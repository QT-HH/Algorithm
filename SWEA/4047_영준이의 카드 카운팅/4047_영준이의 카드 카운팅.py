import sys
sys.stdin = open('input.txt')

def game():
    for i in range(0, len(cards), 3):
        if cards[i + 1:i + 3] in deck[cards[i]]:
            return 'ERROR'
        deck[cards[i]].append(cards[i + 1:i + 3])
    result = []
    for i in deck:
        result.append(str(13-len(deck[i])))

    return ' '.join(result)

test = int(input())
for t in range(1,test+1):
    cards = input()
    deck = {'S':[],'D':[],'H':[],'C':[]}
    print(f'#{t} {game()}')
