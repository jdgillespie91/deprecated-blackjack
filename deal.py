# Returns an integer between one and seven based on user input.
def get_number_of_players():
    while True:
        try:
            number_of_players = int(raw_input('Please input the number of players (from one to seven): '))
            if (0 < number_of_players < 8):
                break
            else:
                print 'The number of players is out of range. Try again...\n'
        except ValueError:
            print 'The number of players is not an integer. Try again...\n'
        
    print 'Using ' + str(number_of_players) + ' players...\n'
    
    return number_of_players
    
# Returns an integer between one and eight based on user input.
def get_number_of_decks():
    while True:
        try:
            number_of_decks = int(raw_input('Please input the number of decks to be used (from one to eight): '))
            if (0 < number_of_decks < 9):
                break
            else:
                print 'The number of decks is out of range. Try again...\n'
        except ValueError:
            print 'The number of decks is not an integer. Try again...\n'
    
    print 'Using ' + str(number_of_decks) + ' decks...\n'

    return number_of_decks
    
# Takes an integer number_of_decks and returns a list of lists that is the shuffled playing deck.
from random import shuffle
def create_playing_deck(number_of_decks):
    playing_deck = []
    rank = ['A', '2', '3', '4', '5', '6', '7', '8', '9', 'T', 'J', 'Q', 'K']
    suit = [u'\u2660', u'\u2661', u'\u2662', u'\u2663']
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

# Returns a list of list of lists. The innermost list corresponds to a single card. The middle list corresponds to a single hand. The outermost list corresponds to all hands on the table.
def deal(playing_deck, number_of_players):
    number_of_hands = number_of_players + 1
    
    list_of_hands = [[[] for i in xrange(2)] for i in xrange(number_of_hands)]
    
    for i in xrange(2*number_of_hands):
        player_index = i%number_of_hands
        card_index = i/number_of_hands
        list_of_hands[player_index][card_index] = playing_deck[0]
        del playing_deck[0]
        
    return list_of_hands
