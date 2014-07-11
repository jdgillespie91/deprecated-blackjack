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
