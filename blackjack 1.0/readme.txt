Blackjack 1.0

---------------------------------------------
Contents
---------------------------------------------

1. Introduction
2. Rules
3. Our Objectives
3.a. The Blackjack Game
3.a.i. Create Playing Deck
3.a.ii. Deal
3.b. The Learning Algorithm



---------------------------------------------
1. Introduction
---------------------------------------------

We aim to create a learning algorithm that will find empirically the optimal blackjack strategy.

---------------------------------------------
2. Rules
---------------------------------------------

In order to build the game, we begin with a simplified version of the rules. We will add features as appropriate. With that in mind, a description of the rules is given (this description should be updated as features are added).

The objective of the game is to win money by obtaining a hand with a total that is both higher than the dealer's hand and less than or equal to 21.

Picture cards have value 10 and aces may be one (a "soft ace") or 11 (a "hard ace"). In the instance that a hard total is bust, the soft total will always be taken. 

Bets are placed before any cards are seen. The deal then takes place. A card is dealt face up to the player and then to the dealer. A second card is dealt face up to the player and face down to the dealer. The dealer reveals his second card if and only if he has blackjack (an ace and a 10).

Action falls to the player. Whilst his total is less than or equal to 21, he may

1. Hit
The player receives an additional card.

2. Stand
Action moves to the next player (or dealer if there are no more players).

If the player busts (his total becomes more than 21), he loses his stake to the dealer.

Action then moves to the dealer. Whilst his total is less than 17, he must hit. We use the rule that the dealer must hit a soft 17 [1]. With a total of 17 (not soft) or higher, the dealer stands (or is bust). 

Totals are then compared. If the player has the higher total, the player keeps his bet and the dealer must give the player an amount equal to it. If the dealer has the higher total, the player loses his bet to the dealer. If their totals are equal, the bet returns to the player. The only exception to this is blackjack. A blackjack beats any non-blackjack 21 and if the player beats the dealer with a blackjack, the dealer must pay the player one-and-a-half times his bet. 

See http://en.wikipedia.org/wiki/Blackjack#Rules_of_play_at_casinos for the rules that we will ultimately follow. The one key difference is that betting on other players is disregarded. 

---------------------------------------------
3. Our Objectives
---------------------------------------------

Broadly speaking, we have two objectives; first, write the blackjack game, and second, write the learning algorithm.

--------------------------------
3.a. The Blackjack Game
--------------------------------             

The development of the game should be broken down into the following modules (each module should be independent of the others and hence can be worked on individually):

-------------------             
3.a.i. Deal
-------------------

The deal will give two cards to the dealer and each player. The players' cards and the first of the dealer's cards will be revealed to the table. The number of players and decks is variable and is input by the user.

See deal.py for the relevant functions in this module.

get_number_of_players returns an integer between one and seven based on user input. After three attemps, the value will default to three automatically.

get_number_of_decks returns an integer between one and eight based on user input. After three attemps, the value will default to three automatically.

create_playing_deck takes the number of decks in play as an argument and returns a shuffled list of lists that is the playing deck. Each inner list corresponds to a card and contains four elements; the first is the rank, the second is the suit, the third is the value and the fourth is a unique identifier. The meanings of the first three are as you would expect (although it should be noted that Aces begin with the value of 11 and are decreased to 1 if necessary). The fourth is to ensure that the deck is built correctly and used only for debugging purposes.

deal_playing_deck takes a playing deck and number of players as arguments, deals as appropriate and prints the required information.



---------------------------------------------
Footnotes
---------------------------------------------
[1] According to http://en.wikipedia.org/wiki/Blackjack#Rule_variations_and_their_consequences_for_the_house_edge, this gives the dealer an edge compared to if he were to stand on soft 17. Dealing with the worst-case scenario is good for us (since the performance of any strategy we find can then only improve).