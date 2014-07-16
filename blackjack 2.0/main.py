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

# Jake 17/07/14 - game(...) in general is quite messy. The functionality is okay though. Feel free to clean it up - in particular, note where it's difficult to follow my logic. This will highlight what specifically needs cleaning up.
def game(manual_flag, number_of_players, number_of_decks, number_of_automated_runs = 1):
    deck = get_deck(number_of_decks)
    number_of_hands = get_number_of_hands(number_of_players)
    
    list_of_hands = do_deal(deck, number_of_hands)
    
    # Jake 16/07/14 - I think the logic here could be made less repetitive but I can't work out how! Any ideas?
    list_of_hands_totals = [0]*number_of_hands # Initialise a zero array to be updated in the following loop.
    if manual_flag:
        print_list_of_hands(list_of_hands)
        for player_index in number_of_players:
            list_of_hands_totals[player_index] = player_turn_manual(list_of_hands[player_index])
    else:
        for player_index in number_of_players:
            list_of_hands_totals[player_index] = player_turn_auto(list_of_hands[player_index])
            
    dealer_index = number_of_hands
    list_of_hands_totals[dealer_index] = dealer_turn(list_of_hands[dealer_index])
    
    list_of_outcomes = do_determine_outcomes(list_of_hands_totals)
    
    return list_of_outcomes
    
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

