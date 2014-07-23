# -*- coding: utf-8 -*-
## Functions ###

class Card:
    def __init__(self,value,suit,rank):
        self.value = value
        self.suit = suit
        self.rank = rank

    def isSoftAce(self):
        if self.value == 11:
            return True
        else:
            return False

    def makeHardAce(self):
        if not self.isSoftAce():
            print '****ERROR**** Tried to make a hard ace out of a ' + str(self.value)
        else:
            self.value = 1

def play_blackjack(manual_flag, number_of_games = 1):
    number_of_players = get_number_of_players()
    number_of_decks = get_number_of_decks()
    list_of_game_results = [0]*number_of_games*number_of_players

    for game in xrange(number_of_games):
        game_results = game(manual_flag, number_of_players, number_of_decks)
        if manual_flag:
            print_results(game_results)
        else:
            list_of_game_results[number_of_players*game, number_of_players*(game+1) - 1] = game_results # Assign game_results to earliest unassigned position in list_of_game_results.

def get_number_of_players():
    undecided = True
    while undecided:
        print
        decision = raw_input("How many players (1-8)? \n")
        try:
            decision = int(decision)
            if decision in range(1,8):
                return decision
            else:
                print "Choice not available"
        except ValueError:
            print "Not an integer"

def get_number_of_decks():
    undecided = True
    while undecided:
        print
        decision = raw_input("How many decks (1-8)? \n")
        try:
            decision = int(decision)
            if decision in range(1,8):
                return decision
            else:
                print "Choice not available"
        except ValueError:
            print "Not an integer"

def game(manual_flag, number_of_players, number_of_decks):
    deck = get_deck(number_of_decks)
    hands = do_deal_deck(deck, number_of_players)
    hand_totals = [0]*(number_of_players + 1) # number_of_players + 1 includes dealer.

    for player_index in xrange(number_of_players)
        player_hand = hands[player_index]
        if manual_flag:
            player_total = do_player_turn_manual(player_hand)
        else:
            player_total = do_player_turn_auto(player_hand)

        hand_totals[player_index] = player_total # Removed append for speed and consistency with assigning hand_totals[dealer_index] = dealer_total.

    dealer_index = number_of_players
    dealer_hand = hands[dealer_index]
    dealer_total = do_dealer_turn(dealer_hand)
    hand_totals[dealer_index] = dealer_total

    results = do_determine_results(hand_totals)

    return results

def print_results(list_of_results):

def get_deck(number_of_decks):

def get_number_of_hands(number_of_players):

def do_deal(deck):

def generate_card_pictures(hand):
    # Makes playing cards like so:
    # ╔═══╗╔═══╗                  
    # ║ 2 ║║ 5 ║                  
    # ║ ♦ ║║ ♣ ║
    # ╚═══╝╚═══╝
    
    line_card_top = u""    
    line_card_rank = u""
    line_card_suit = u""
    line_card_bottom = u""

    for card in hand:
        line_card_top += u"╔═══╗"
        line_card_rank += u"║ {0} ║".format(card.rank)
        line_card_suit += u"║ {0} ║".format(card.suit)
        line_card_bottom += u"╚═══╝"     
 
    card_pictures = [line_card_top,line_card_rank,line_card_suit,line_card_bottom]
    
    return card_pictures

def print_hands(list_of_hands):
    number_of_players = get_number_of_players(list_of_hands)
    dealer_hand = list_of_hands[number_of_players]

    line_dealer_label = u""
    line_dealer_hand = u""
    line_player_hands = u""
    line_player_labels = u""
    line_current_player_arrows = u""
    line_current_player_total = u"TOTAL: {0}"

    player_strings = []
    for player in range(number_of_players):
        hand = list_of_hands[player]
        player_cards_string = u""
        
        for card in hand:
            player_cards_string += card.rank+card.suit
            
        player_strings.append("|"+player_cards_string+"|") # e.g |A♦2♣5♣|
        
    dealer_cards_string = u""
    for card in dealer_hand:
        dealer_cards_string += card.rank + card.suit

    player_labels = []
    for player in xrange(number_of_players):
        player_string = player_strings[player]
        player_label = ("P{0}".format(player)).center(len(player_string))
        player_labels.append(player_label)

        line_player_hands += player_string
        line_player_labels += player_label

    output_width = len(line_player_hands)

    dealer_up_card_string = dealer_hand[0].rank + dealer_hand[0].suit
    
    line_dealer_label = "D".center(output_width)
    line_dealer_hand = u"|{0} ?|".format(dealer_up_card_string) # e.g |A♦ ?|
        
    # card_pictures = generate_card_pictures(list_of_hands[current_player])

    print
    print "".center(output_width,'#')+"\n"
    print line_dealer_label
    print line_dealer_hand.center(output_width)
    print "".center(output_width,'=')
    print line_player_hands
    print line_player_labels
    print
    print "".center(output_width,'#')
    print

def player_turn_manual(hand):
    STAND = 0
    HIT = 1

    is_turn_finished = False
    while not is_turn_finished:
        print_list_of_hands(hands)
        print_hand(hand)
        decision = get_decision(hand)

        if decision == STAND:
            do_player_stand()
            is_turn_finished = True

        elif decision == HIT:
            do_hit()
            if get_hand_total(hand) == BUST:
                is_turn_finished = True

    return get_hand_total(hand)

def player_turn_auto(hand):
    STAND = 0
    HIT = 1

    is_turn_finished = False
    while not is_turn_finished:
        decision = get_decision(hand)

        if decision == STAND:
            do_player_stand()
            is_turn_finished = True

        elif decision == HIT:
            do_hit()
            if get_hand_total(hand) == BUST:
                is_turn_finished = True

    return get_hand_total(hand)

def dealer_turn(hand):
    BUST = 0
    if is_blackjack(hand):
        return 1

    while True:
        hand_total = get_hand_total(hand)
        if hand_total > 21:
            is_bust = True
            for card in hand:
                if card.isSoftAce():
                    card.makeHardAce()
                    is_bust = False
                    break
            if is_bust:
                return BUST
        else:
            if hand_total > 17:
                return hand_total
            elif hand_total == 17:
                is_hand_hard = True
                for card in hand
                    if card.isSoftAce():
                        card.makeHardAce
                        is_hand_hard = False
                        do_hit(hand, deck)
                        break
                if is_hand_hard:
                    return hand_total
            elif hand_total < 17:
                do_hit(hand, deck)

def is_blackjack(hand):
    card_one = hand[0]
    card_two = hand[1]
    
    if card_one.value == 11:
        if card_two.value == 10:
            return True
        else:
            return False
    elif card_one.value == 10:
        if card_two.value == 11:
            return True
        else:
            return False
    else:
        return False

def do_hit(hand, deck):

def get_available_decisions(hand):
    # we know that the player can not be bust now
    # the only time he cannot hit is when he has 21
    STAND = [0, 'Stand']
    HIT = [1, 'Hit']
    SPLIT = [2, 'Split']
    decisions = [STAND] # one may stand at any time
    
    hand_total = get_hand_total(hand)
    if hand_total < 21:
        decisions.append(HIT)

    # if splits are allowed include the following
    #if len(hand) == 2 and hand[0].value == hand[1].value:
        #decisions.append(SPLIT)

    return decisions
    
def get_decision(hand):
    if manual_flag:
        available_decisions = get_available_decisions(hand)
        available_integers = []
            
        undecided = True
        while undecided:
            print
            print "Please choose an action: \n"
            print
            
            for decision in available_decisions:
                decision_number, decision_name = decision[0], decision[1]
                print "{0}. {1}".format(decision_number, decision_name)
                available_integers.append(decision_number)
                
            print
            decision = raw_input("Enter choice number-->")
            try:
                decision = int(decision)
                if decision in available_integers:
                    return decision
                else:
                    print "Choice not available"
            except ValueError:
                print "Not an integer"
        

def do_determine_results(list_of_hand_totals):
    DEALER_WIN = 0
    DRAW = 1
    PLAYER_WIN = 2

    results = []
    dealer_total = list_of_hand_totals.pop()
    
    for player_total in list_of_hand_totals:
        if player_total < dealer_total:
            results.append(DEALER_WIN)
        elif player_total == dealer_total:
            results.append(DRAW)
        elif player_total > dealer_total:
            results.append(PLAYER_WIN)

    return results

def get_hand_total(hand):
    total = 0
    for card in hand:
        total += card.value
    return total

## Execution ###

play_blackjack(True)

