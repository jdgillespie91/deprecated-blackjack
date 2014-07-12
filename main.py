from deal import *
from playing_deck import *
from plays import *

# Determine number of players based on user input.
# number_of_players = get_number_of_players()
number_of_players = 4
number_of_players = get_number_of_players()
# number_of_players = 3

# Determine number of decks based on user input.
number_of_decks = get_number_of_decks()
# number_of_decks = 3

# Create playing deck.
playing_deck = create_playing_deck(number_of_decks)

# Deal hands.
list_of_hands = deal_playing_deck(playing_deck, number_of_players)

list_of_totals = [None]*number_of_players
for player in range(number_of_players):
    print "\n\nPlayer {0}'s turn".format(player)
    player_hand = list_of_hands[player]
    #print_hand(player_hand)
    player_finished = False
    while not player_finished:
        display_current_state(list_of_hands,player)
        return_value = turn(playing_deck, player_hand)
        player_finished = return_value[0]
        hand = return_value[1]
        
    list_of_totals[player] = get_total(hand)

raw_input("\nPress enter for dealer's turn.")

# Fix hand.
#print list_of_hands[number_of_players]
#list_of_hands[number_of_players][0] = ['8', u'\u2662', 8, 1]
#list_of_hands[number_of_players][1] = ['6', u'\u2662', 6, 1]
#playing_deck[0] = ['3', u'\u2662', 3, 1]

# Dealer Plays.
outcome = dealer_play(playing_deck, list_of_hands[number_of_players])

if outcome == 1:
    print 'The dealer has blackjack.'
    outcome = 21
elif outcome == 2:
    print 'The dealer is bust.'
elif outcome in xrange(17,22):
    print 'The dealer stands on ' + str(outcome)
else:
    print 'Error: outcome has taken an unexpected value.'
print '\n'

#Display results of game
#Issue - doesn't handle bust dealer+bust player combo well
for player in range(number_of_players):
    player_total = list_of_totals[player]
    if 21>=player_total>=outcome:
        print 'Player {0} beats the dealer with {1}>={2}'.format(player,player_total,outcome)
    else:
        print 'Dealer beats player {0}, {1}>{2}'.format(player,outcome,player_total)
