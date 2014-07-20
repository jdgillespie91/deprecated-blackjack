iterator = 0

# bj_1
card_list_one = [[10,'K'], [10,'Q'], [10,'J'], [10,'10']]
card_list_two = [[11,'A']]
suit_list_one = ['Spades', 'Hearts', 'Diamonds', 'Clubs']
suit_list_two = ['Spades', 'Hearts', 'Diamonds', 'Clubs']
test_string = """def test_{8:04d}_{0}{1}(self):
    hand = [Card({2}, '{3}', '{4}'),Card({5}, '{6}', '{7}')]
    answer = is_blackjack(hand)

    self.assertEqual(answer, True)
    """

for card_one in card_list_one:
    for card_two in card_list_two:
        for suit_one in suit_list_one:
            for suit_two in suit_list_two:
                iterator += 1
                print test_string.format(card_one[1], card_two[1], card_one[0], suit_one, card_one[1], card_two[0], suit_two, card_two[1], iterator)

# bj_2
card_list_one = [[11,'A']]
card_list_two = [[10,'K'], [10,'Q'], [10,'J'], [10,'10']]
suit_list_one = ['Spades', 'Hearts', 'Diamonds', 'Clubs']
suit_list_two = ['Spades', 'Hearts', 'Diamonds', 'Clubs']
test_string = """def test_{8:04d}_{0}{1}(self):
    hand = [Card({2}, '{3}', '{4}'),Card({5}, '{6}', '{7}')]
    answer = is_blackjack(hand)

    self.assertEqual(answer, True)
    """

for card_one in card_list_one:
    for card_two in card_list_two:
        for suit_one in suit_list_one:
            for suit_two in suit_list_two:
                iterator += 1
                print test_string.format(card_one[1], card_two[1], card_one[0], suit_one, card_one[1], card_two[0], suit_two, card_two[1], iterator)