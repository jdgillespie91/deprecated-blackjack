# Prints the contents of a hand. The first index must refer to each card and the second index must refer to the rank and suit.
def print_hand(hand):
    for i in xrange(len(hand)):
        print hand[i][0] + hand[i][1],
    print
