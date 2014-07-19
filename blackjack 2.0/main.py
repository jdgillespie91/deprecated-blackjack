## Functions ###

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

def player_turn_auto(hand):

def dealer_turn(hand):
    if is_blackjack(hand):
        return 1
    
    while True:
        total = get_hand_value(hand) # Alternatively, we could call this outside of the while loop and increment the total each time we hit. It doesn't read as well but saves computation time.
        if total > 21:
            # Make this readable.
            if 1 or 14 or 27 or 40 in hand:
                # set soft ace to 0.
            else:
                return 0
        else:
            if total > 17:
                return total
            elif total == 17:
                # Make this readable.
                if 1 or 14 or 27 or 40 in hand:
                    # set soft ace to 0.
                    do_hit(hand, deck)
                else:
                    return total
            else:
                do_hit(hand, deck)
    
def is_blackjack(hand):
    
def do_hit(hand):

def do_determine_results(list_of_hands_totals):

def get_card_value(card):



## Execution ###

play_blackjack(True)

