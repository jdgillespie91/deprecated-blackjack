def get_number_of_players():
    count = 0
    
    while (count < 3):
        try:
            number_of_players = int(raw_input('Please input the number of players (from one to seven): '))
            if (0 < number_of_players < 8):
                break
            else:
                count += 1
                if (count == 3):
                    print 'You have exceeded the number of attempts. Defaulting to three players.\n'
                    number_of_players = 3
                else:
                    print 'The number of players is out of range. Try again...\n'
        except ValueError:
            count += 1
            if (count == 3):
                print 'You have exceeded the number of attempts. Defaulting to three players.\n'
                number_of_players = 3
            else:
                print 'The number of players is not an integer. Try again...\n'
        
    print 'Using ' + str(number_of_players) + ' players...\n'
    
    return number_of_players
    
def get_number_of_decks():
    count = 0
    
    while (count < 3):
        try:
            number_of_decks = int(raw_input('Please input the number of decks to be used (from one to eight): '))
            if (0 < number_of_decks < 9):
                break
            else:
                count += 1
                if (count == 3):
                    print 'You have exceeded the number of attempts. Defaulting to three decks.\n'
                    number_of_decks = 3
                else:
                    print 'The number of decks is out of range. Try again...\n'
        except ValueError:
            count += 1
            if (count == 3):
                print 'You have exceeded the number of attempts. Defaulting to three decks.\n'
                number_of_decks = 3
            else:
                print 'The number of decks is not an integer. Try again...\n'
    
    print 'Using ' + str(number_of_decks) + ' decks...\n'

    return number_of_decks
    
from random import shuffle
def create_playing_deck(number_of_decks):
    playing_deck = []
    rank = ['A', '2', '3', '4', '5', '6', '7', '8', '9', 'T', 'J', 'Q', 'K']
    suit = [u'\u2666', u'\u2665', u'\u2660', u'\u2663']
    #diamond/heart/spade/club
    unique_id = 0

    for i in xrange(number_of_decks):
        for j in rank:
            for k in suit:
                unique_id += 1
                if j == 'A':
                    playing_deck.append([j, k, 11, unique_id])
                elif j == 'T':
                    playing_deck.append([j, k, 10, unique_id])
                elif j == 'J':
                    playing_deck.append([j, k, 10, unique_id])
                elif j == 'Q':
                    playing_deck.append([j, k, 10, unique_id])
                elif j == 'K':
                    playing_deck.append([j, k, 10, unique_id])
                else:
                    playing_deck.append([j, k, int(j), unique_id])
    
    shuffle(playing_deck)
    
    return playing_deck    

from random_functions import *
def deal_playing_deck(playing_deck, number_of_players):
    number_of_hands = number_of_players + 1
    
    list_of_hands = [[[] for i in xrange(2)] for i in xrange(number_of_hands)]
    
    for i in xrange(2*number_of_hands):
        player_index = i%number_of_hands
        card_index = i/number_of_hands
        list_of_hands[player_index][card_index] = playing_deck[0]
        del playing_deck[0]
        
    return list_of_hands
