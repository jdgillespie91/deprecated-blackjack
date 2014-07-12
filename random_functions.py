def print_hand(hand):
    for i in xrange(len(hand)):
        print hand[i][0] + hand[i][1],
    print

def print_card(hand, card_index):
    print hand[card_index][0] + hand[card_index][1],