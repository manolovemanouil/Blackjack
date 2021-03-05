import time
from random import random
from random import seed

newDeck = {0 : "Ace of Spades",
           1 : "2 of Spades",
           2 : "3 of Spades",
           3 : "4 of Spades",
           4 : "5 of Spades",
           5 : "6 of Spades",
           6 : "7 of Spades",
           7 : "8 of Spades",
           8 : "9 of Spades",
           9: "10 of Spades",
           10: "Jack of Spades",
           11: "Queen of Spades",
           12: "King of Spades",
           13: "Ace of Diamonds",
           14: "2 of Diamonds",
           15: "3 of Diamonds",
           16: "4 of Diamonds",
           17: "5 of Diamonds",
           18: "6 of Diamonds",
           19: "7 of Diamonds",
           20: "8 of Diamonds",
           21: "9 of Diamonds",
           22: "10 of Diamonds",
           23: "Jack of Diamonds",
           24: "Queen of Diamonds",
           25: "King of Diamonds",
           26: "King of Clubs",
           27: "Queen of Clubs",
           28: "Jack of Clubs",
           29: "10 of Clubs",
           30: "9 of Clubs",
           31: "8 of Clubs",
           32: "7 of Clubs",
           33: "6 of Clubs",
           34: "5 of Clubs",
           35: "4 of Clubs",
           36: "3 of Clubs",
           37: "2 of Clubs",
           38: "Ace of Clubs",
           39: "King of Hearts",
           40: "Queen of Hearts",
           41: "Jack of Hearts",
           42: "10 of Hearts",
           43: "9 of Hearts",
           44: "8 of Hearts",
           45: "7 of Hearts",
           46: "6 of Hearts",
           47: "5 of Hearts",
           48: "4 of Hearts",
           49: "3 of Hearts",
           50: "2 of Hearts",
           51: "Ace of Hearts"}

deckVal = {0 : -1,
           1 : 2,
           2 : 3,
           3 : 4,
           4 : 5,
           5 : 6,
           6 : 7,
           7 : 8,
           8 : 9,
           9: 10,
           10: 10,
           11: 10,
           12: 10,
           13: -1,
           14: 2,
           15: 3,
           16: 4,
           17: 5,
           18: 6,
           19: 7,
           20: 8,
           21: 9,
           22: 10,
           23: 10,
           24: 10,
           25: 10,
           26: 10,
           27: 10,
           28: 10,
           29: 10,
           30: 9,
           31: 8,
           32: 7,
           33: 6,
           34: 5,
           35: 4,
           36: 3,
           37: 2,
           38: -1,
           39: 10,
           40: 10,
           41: 10,
           42: 10,
           43: 9,
           44: 8,
           45: 7,
           46: 6,
           47: 5,
           48: 4,
           49: 3,
           50: 2,
           51: -1}


k = 0
deck = []

for x in range(0, 312):
    if k >=52:
        k = 0
    deck.append(k)
    k = k + 1

#print(deck)

millis = int(round(time.time() * 1000))

seed(millis)


def fisher_yates_shuffle(deck):

    i = 311

    while True:
        if i < 0:
            break

        j = int(random()*311)

        temp = deck[i]
        deck[i] = deck[j]
        deck[j] = temp

        i = i - 1

def getValue(arr):

    retval = 0
    a = arr[:]
    for i,element in enumerate(a):
        a[i] = deckVal[element]
    a.sort()
    a.reverse()

    for eval in a:

        if eval == -1:
            if (retval + 11) > 21:
                retval = retval + 1
            else:
                retval = retval + 11
        else:
            retval = retval + eval
    return retval

fisher_yates_shuffle(deck)

#print(deck)



player = []
dealer = []

player.append(deck.pop())
dealer.append(deck.pop())
player.append(deck.pop())
dealer.append(deck.pop())

#print("Player:")
#print(newDeck[player[0]], " ", newDeck[player[1]])

pval = getValue(player)
#print("Player Value: ", pval)

#print("Dealer:")
#print(newDeck[dealer[0]], " ", newDeck[dealer[1]])

dval = getValue(dealer)
#print("Dealer Value: ", dval)






