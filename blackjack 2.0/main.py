### Functions ###

def play_blackjack(manual_flag):
    number_of_players = get_number_of_players()
    number_of_decks = get_number_of_decks()
    if manual_flag:
        list_of_outcomes = game(manual_flag, number_of_players, number_of_decks) # In manual mode, execute game(...) once only.
        print_outcomes(list_of_outcomes)
    else:
        number_of_automated_runs = get_number_of_automated_runs()
        list_of_outcomes = game(manual_flag, number_of_players, number_of_decks, number_of_automated_runs)
    
    return list_of_outcomes
    
def get_number_of_players():
    
def get_number_of_decks():
    
def get_number_of_automated_runs():
    
def game(manual_flag, number_of_players, number_of_decks, number_of_automated_runs = 1):
    deck = get_deck(number_of_decks)
    hands = do_deal_deck(deck, number_of_players)
    player_indices = [0] * number_of_players
    dealer_index = number_of_players
    
    # The repetition here suggests there is room for improvement in the logic.
    if manual_flag:
        print_hands(hands)
        for player_index in player_indices:
            player_hand = hands[player_index]
            player_total = do_player_turn_manual(player_hand)
            hand_totals[player_index] = player_total # Consider using append function since it might read better.
    else:
        for player_index in player_indices:
            player_hand = hands[player_index]
            player_total = do_player_turn_auto(player_hand)
            hand_totals[player_index] = player_total # Consider using append function since it might read better.
    
    dealer_hand = hands[dealer_index]
    dealer_total = do_dealer_turn(dealer_hand)
    hand_totals[dealer_index] = dealer_total
    
    outcomes = do_determine_outcomes(hand_totals)
    
    return outcomes
    
def print_outcomes(list_of_outcomes):
    
def get_deck(number_of_decks):
    
def get_number_of_hands(number_of_players):
    
def do_deal(deck):
    
def print_list_of_hands(list_of_hands):
    
def player_turn_manual(hand):

def player_turn_auto(hand):

def dealer_turn(hand):
    
def do_determine_outcomes(list_of_hands_totals):
    
def get_card_value(card):



### Execution ###

play_blackjack(True)

