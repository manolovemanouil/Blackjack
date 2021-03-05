import deckshuffle

pair_list = {
"ace_pair" : [0,13,38,51],
"two_pair" : [1,14,37,50],
"three_pair" : [2,15,36,49],
"four_pair" : [3,16,35,48],
"five_pair" : [4,17,34,47],
"six_pair" : [5,18,33,46],
"seven_pair" : [6,19,32,45],
"eight_pair" : [7,20,31,44],
"nine_pair" : [8,21,30,43],
"ten_pair" : [9,22,29,42],
"jack_pair" : [10,23,28,41],
"queen_pair" : [11,24,27,40],
"king_pair" : [12,25,26,39]}


def has_pair(hand):

    card1 = hand[0]
    card2 = hand[1]

    for key in pair_list:

        if card1 in pair_list[key]:
            if card2 in pair_list[key]:
                return True
            else:
                return False


    return False


