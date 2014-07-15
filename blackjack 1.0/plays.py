# Checks a hand for blackjack. Returns 1 if blackjack and 0 otherwise.
def check_blackjack(hand):
    if hand[0][2]+hand[1][2] == 21:
        return 1
    else:
        return 0      
        
# Counts the number of hard aces in a hand.
def number_of_hard_aces(hand):
    number_of_hard_aces = 0
    
    for card in hand:
        if card[2]==11:
            number_of_hard_aces += 1
            
    return number_of_hard_aces

# Takes the playing deck and the hitting hand. A card is taken from the top of the playing deck and added to the hitting hand.
def hit(playing_deck, hand):
    hand.append(playing_deck[0])
    del playing_deck[0]

def stand(hand):
    total = 0
    for card in hand:
        total += card[2]
        
    print "The player (or dealer?) stands on " + str(total)
    
    return total
    
def is_bust(hand):
    total = 0
    for card in hand:
        total += card[2]
        
    is_bust = False

    if (total > 21):
        is_bust = True
    # currently vulnerable if hit on 21 (if we hit on 21 and get an ace whilst having a soft ace in our hand, we would be declared bust although we aren't).
        for card in hand:
            if card[2] == 11:
                card[2] = 1
                is_bust = False
                break
    
    return is_bust
        
def turn(playing_deck, hand):
    print '1. Hit'
    print '2. Stand'
    count = 0
    
    while (count < 3):
        try:
            decision = int(raw_input('Decision: '))
            if (decision not in [1,2]):
                count += 1
                if (count == 3):
                    print 'You have exceeded the number of attempts. Defaulting to stand.\n'
                    decision = 2
                else:
                    print 'Input does not correspond to a decision. Try again...\n'
            else:
                break
        except ValueError:
            count += 1
            if (count == 3):
                print 'You have exceeded the number of attempts. Defaulting to stand.\n'
                decision = 2
            else:
                print 'Input does not correspond to a decision. Try again...\n'
    
    finished = False
    if (decision == 1):
        hit(playing_deck, hand)
        if is_bust(hand):
            finished = True
            print 'We are bust!'
        # if bust, finished = True
    elif (decision == 2):
        stand(hand)
        finished = True
    else:
        print 'Unexpected decision! We have a bug somewhere.'
    
    print_hand(hand)
    return finished, hand
    
# Takes dealer hand and returns 1 if blackjack, 2 if bust, the standing total if between 17 and 21 inclusive and -1 otherwise (i.e. error code).
from random_functions import *
def dealer_play(playing_deck, hand):
    card_index = 0
    outcome = -1

    print_hand(hand)
    if check_blackjack(hand):
        outcome = 1
    else:
        total = hand[0][2] + hand[1][2]
        while True:
            if total > 21:
                if card_index < len(hand):
                    if hand[card_index][2] == 11:
                        hand[card_index][2] = 1
                        total -= 10
                        card_index += 1
                    else:
                        card_index += 1
                else:
                    outcome = 2
                    break
            else:
                if total < 17:
                    hit(playing_deck, hand)
                    print_hand(hand)
                    total += hand[len(hand)-1][2]
                else:
                    if total == 17:
                        print 'total = 17'
                        for card in hand:
                            if card[2]==11:
                                print 'Change ace.'
                            else:
                                print 'Hand does not need to change.'
                                outcome = total
                                return outcome
                    else:
                        print 'total > 17 (and less than or equal to 21).'
                        outcome = total
                        break   
    return outcome