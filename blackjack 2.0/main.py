### Functions ###

def play_blackjack(manual_flag):
    number_of_players = get_number_of_players()
    number_of_decks = get_number_of_decks()
    if manual_flag:
        list_of_outcomes = game(number_of_players, number_of_decks) # In manual mode, execute game(...) once only.
        print_outcomes(list_of_outcomes)
    else:
        number_of_automated_runs = get_number_of_automated_runs()
        list_of_outcomes = game(number_of_players, number_of_decks, number_of_automated_runs)
    
    return list_of_outcomes
    
def get_number_of_players():
    
def get_number_of_decks():
    
def get_number_of_automated_runs():
    
def game(number_of_players, number_of_decks, number_of_automated_runs = 1):
    deck = get_deck(number_of_decks)
    list_of_hands = deal(deck)
    
def print_outcomes(list_of_outcomes):
    
def get_deck(number_of_decks):
    
def deal(deck):
    
def get_card_value(card):



### Execution ###

play_blackjack(True)