# -*- coding: utf-8 -*-
def print_hand(hand):
    for i in xrange(len(hand)):
        print_card(hand,i)
    print

def print_card(hand, card_index):
    print hand[card_index][0] + hand[card_index][1],
	
def get_total(hand):
    total = 0
    for card in hand:
        total += card[2]
    return total

# For windows users, if os.system('clear') causes problems, try commenting it out and using os.system('cls') instead. If that doesn't work also, just comment out both.
import os
def clear_screen():
    raw_input("Press Enter to continue...")
    if (os.name) == 'posix':
            os.system('clear')
    elif (os.name) == 'nt':
            os.system('cls')

def generate_card_pictures(hand):
    #Makes playing cards like so:
    #╔═══╗╔═══╗                  
    #║ 2 ║║ 5 ║                  
    #║ ♦ ║║ ♣ ║
    #╚═══╝╚═══╝
    
    line_card_rank = u""
    line_card_suit = u""
    number_of_cards = len(hand)

    line_card_top =         u"╔═══╗"*number_of_cards
    for card in hand:
        line_card_rank +=   u"║ {0} ║".format(card[0])
        line_card_suit +=   u"║ {0} ║".format(card[1])
        
    line_card_bottom =      u"╚═══╝"*number_of_cards 
    
    return [line_card_top,line_card_rank,line_card_suit,line_card_bottom]

def display_current_state(list_of_hands, current_player):
    #clear() #would be nice to clear the console here
    no_of_players = len(list_of_hands)-1
    dealer = no_of_players
    
    no_of_cards = 0
    player_strings = []
    player_labels = []
    
    line_dealer_label = u""
    line_dealer_hand = u""
    line_player_hands = u""
    line_player_labels = u""
    line_current_player_arrows = u""
    line_current_player_total = u"TOTAL: {0}"
    
    for player in range(no_of_players):
        hand = list_of_hands[player]
        player_string = u"|"
        for card in hand:
            player_string+=card[0]+card[1]
            no_of_cards+=1
        player_strings.append(player_string+"|")
        
    dealer_string = ""
    for card in list_of_hands[dealer]:
        dealer_string+=card[0]+card[1]

    for player in range(no_of_players):
        player_string = player_strings[player]
        line_player_hands += player_string
        player_label = ("P{0}".format(player)).center(len(player_string))
        player_labels.append(player_label)
        line_player_labels += player_label

    output_width = len(line_player_labels)
    line_dealer_label = "D".center(output_width)
    line_dealer_hand = u"|{0}|".format(dealer_string)
    for player in range (current_player):
        line_current_player_arrows += " "*len(player_labels[player])
    line_current_player_arrows += u" \u2191\u2191".center(len(player_labels[current_player]))
    line_current_player_total = line_current_player_total.format(get_total(list_of_hands[current_player])).center(output_width)

    card_pictures = generate_card_pictures(list_of_hands[current_player])



    print
    print "".center(output_width,'#')+"\n"
    print line_dealer_label
    print line_dealer_hand.center(output_width)
    print "".center(output_width,'=')
    print line_player_hands
    print line_player_labels
    print line_current_player_arrows
    print "".center(output_width,'#')
    print
    for card_line in card_pictures:
        print card_line.center(output_width)
    print line_current_player_total
    print
    print "".center(output_width,'#')+"\n"
    
def display_current_state_edit(list_of_hands, ):
    
