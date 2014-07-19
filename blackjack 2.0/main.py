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
            list_of_game_results[number_of_players*game, number_of_players*(game+1) - 1] = game_results # Assign game_results to earliest unassigned position in list_of_game_results.

def get_number_of_players():

def get_number_of_decks():

def get_number_of_automated_runs():

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

def print_list_of_hands(list_of_hands):

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
                is_hard = True
                for card in hand
                    if card.isSoftAce():
                        card.makeHardAce
                        is_hard = False
                        do_hit(hand, deck)
                        break
                if is_hard:
                    return hand_total
            elif hand_total < 17:
                do_hit(hand, deck)


def is_blackjack(hand):

def do_hit(hand):
    
def get_available_decisions(hand):
    
def get_decision:
    available_decisions = get_available_decisions

def do_determine_results(list_of_hands_totals):

def get_hand_total(hand):

def get_card_value(card):



## Execution ###

play_blackjack(True)

