### Functions ###

def play_blackjack(manual_flag, number_of_games = 1):
    number_of_players = get_number_of_players()
    number_of_decks = get_number_of_decks()
    
    for game in range(number_of_games):
        game_results = game(manual_flag, number_of_players, number_of_decks)
        if manual_flag:
            print_results(list_of_results)
        else:
            list_of_results.append(game_results)
    
def get_number_of_players():
    
def get_number_of_decks():
    
def get_number_of_automated_runs():
    
def game(manual_flag, number_of_players, number_of_decks):
    deck = get_deck(number_of_decks)
    hands = do_deal_deck(deck, number_of_players)
    hand_totals = []
        
    for player_index in range(number_of_players)
        player_hand = hands[player_index]
        if manual_flag:
            player_total = do_player_turn_manual(player_hand)     
        else:
            player_total = do_player_turn_auto(player_hand)   
        
        hand_totals.append(player_total) = player_total
    
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

def player_turn_auto(hand):

def dealer_turn(hand):
    
def do_determine_results(list_of_hands_totals):
    
def get_card_value(card):



### Execution ###

play_blackjack(True)

