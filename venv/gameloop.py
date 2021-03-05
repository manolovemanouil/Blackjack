import deckshuffle
import split
import time

def generate_fresh_deck():
    k = 0
    deck = []

    for x in range(0, 312):
        if k >= 52:
            k = 0
        deck.append(k)
        k = k + 1

    return deck

gamedeck = generate_fresh_deck()

deckshuffle.fisher_yates_shuffle(gamedeck)


def deal_card(player):
    player.append(gamedeck.pop())

player1 = []
dealer = []

def reset():
    player1 = []
    dealer = []

def resetDeck():
    d = generate_fresh_deck()
    deckshuffle.fisher_yates_shuffle(d)

    gamedeck = d

def dealer_moves():

    while True:

        hval = deckshuffle.getValue(dealer)

        if hval < 17:
            deal_card(dealer)
            print("Dealer: ", dealer)
        else:
            break

    return deckshuffle.getValue(dealer)

def print_hand(arr):
    ret = ""
    for element in arr:
        ret = ret + deckshuffle.newDeck[element] + "\t\t"

    return ret
def offer_split():
    while(True):

        answer = input("Would you like to split? y/n\n")

        if answer == 'y' or answer == 'Y':
            return True
        if answer == 'n' or answer == 'N':
            return False
        else:
            print("Invalid response. Try again.\n\n\n")

def player_hit(hand):

    return

while True:
    time.sleep(0.5)
    print("\n\nDEALING...\n\n")
    time.sleep(0.5)
    playerState = 0
    if len(gamedeck) < 52:
        resetDeck()

    player1 = []
    dealer = []

    deal_card(player1)
    print("Player: ", print_hand(player1), " Value: ", deckshuffle.getValue(player1),"\n")
    time.sleep(0.5)
    deal_card(dealer)
    print("Dealer: ", deckshuffle.newDeck[dealer[0]],"\n")
    time.sleep(0.5)
    deal_card(player1)
    print("Player: ", print_hand(player1), " Value: ", deckshuffle.getValue(player1),"\n")
    time.sleep(0.5)
    deal_card(dealer)
    print("Dealer: ", deckshuffle.newDeck[dealer[0]], "\t\tHidden Card","\n")
    time.sleep(0.5)
    #print("ADMIN Dealer: ", print_hand(dealer), " Value: ", deckshuffle.getValue(dealer),"\n")

    if deckshuffle.deckVal[dealer[0]] == 10 or deckshuffle.deckVal[dealer[0]] == -1:
        print("CHECKING FOR BLACKJACK...","\n")
        time.sleep(0.5)

        if deckshuffle.getValue(dealer) == 21:
            print("DEALER BLACKJACK","\n")
            continue

    while True:

        pval = deckshuffle.getValue(player1)

        print("---------------------------------------------\n")

        print("Player: ", print_hand(player1), " Value: ", pval,"\n")
        time.sleep(1)
        print("Dealer: ", deckshuffle.newDeck[dealer[0]], "\t\tHidden Card","\n")
        time.sleep(1)

        if pval > 21:
            print("BUST","\n")
            playerState = -1
            break

        if pval == 21:
            if len(player1) == 2:
                print("BLACKJACK","\n")
                playerState = 1

            break
        if split.has_pair(player1):
            resp = offer_split()

        time.sleep(0.5)

        playerResponse = input("Hit? y/n\n")


        if playerResponse == 'y' or playerResponse == "Y":

            deal_card(player1)
            continue
        elif playerResponse == 'n' or playerResponse == "N":
            break
        else:
            print("Please enter a valid response!","\n")
            time.sleep(0.5)



    if playerState == -1:
        print("DEALER WINS")
        print("\n\n\n")
        continue
    if playerState == 1:
        print("PLAYER WINS")
        print("\n\n\n")
        continue

    dval = dealer_moves()
    pval = deckshuffle.getValue(player1)

    print("Player: ", print_hand(player1), " Value: ", pval,"\n")
    time.sleep(1)
    print("Dealer: ", print_hand(dealer), " Value: ", dval,"\n")
    time.sleep(1)

    if dval > 21:
        print("DEALER BUST","\n")
        print("PLAYER WINS","\n")
        time.sleep(1)
        print("\n\n\n")
        continue

    elif dval == pval:
        print("PUSH")
        time.sleep(1)
        print("\n\n\n")
        continue
    elif dval > pval:
        print("DEALER WINS")
        time.sleep(1)
        print("\n\n\n")
        continue
    else:
        print("PLAYER WINS")
        time.sleep(1)
        print("\n\n\n")
        continue



