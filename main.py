from deal import *
from playing_deck import *
from plays import *

# Determine number of players based on user input.
# number_of_players = get_number_of_players()
number_of_players = 3

# Determine number of decks based on user input.
# number_of_decks = get_number_of_decks()
number_of_decks = 3

# Create playing deck.
playing_deck = create_playing_deck(number_of_decks)

# Deal hands.
list_of_hands = deal(playing_deck, number_of_players)

# Fix hand.
print list_of_hands[number_of_players]
list_of_hands[number_of_players][0] = ['8', u'\u2662', 8, 1]
list_of_hands[number_of_players][1] = ['6', u'\u2662', 6, 1]
playing_deck[0] = ['3', u'\u2662', 3, 1]
print list_of_hands[number_of_players]

# Dealer Plays.
outcome = dealer_play(playing_deck, list_of_hands[number_of_players])

if outcome == 1:
    print 'The dealer has blackjack.'
elif outcome == 2:
    print 'The dealer is bust.'
elif outcome in xrange(17,22):
    print 'The dealer stands on ' + str(outcome)
else:
    print 'Error: outcome has taken an unexpected value.'