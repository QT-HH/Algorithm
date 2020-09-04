import random

cards = [random.randrange(0,10) for i in range(6)]
cards = [5,8,6,6,7,7]
cards.sort()
print(cards)

run = 0
triplet = 0

for i in cards:
    if cards.count(i)>=3:
        for j in range(3):
            cards.remove(i)
        triplet +=1

for i in cards:
    if i+1 in cards and i+2 in cards:
        for j in [i+1,i+2]:
            cards.remove(j)
        run +=1


print(f'triplet : {triplet}, \nrun : {run}')

if triplet+run ==2:
    print(True)
else:
    print(False)