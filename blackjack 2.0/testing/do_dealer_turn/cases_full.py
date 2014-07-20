iterator = 0

# Check totals 4-12.
card_list_one = [[2,'2']]
card_list_two = [[10,'10'], [9,'9'], [8,'8'], [7,'7'], [6,'6'], [5,'5'], [4,'4'], [3,'3'], [2,'2']]
test_string = """def test_{8:04d}_{0}{1}(self):
    hand = [Card({2}, '{3}', '{4}'),Card({5}, '{6}', '{7}')]
    do_dealer_turn(hand)
    
    self.assertEqual(len(hand), 3)
    """

for card_one in card_list_one:
    for card_two in card_list_two:
        iterator += 1
        print test_string.format(card_one[1], card_two[1], card_one[0], 'spades', card_one[1], card_two[0], 'spades', card_two[1], iterator)
         
# Check totals 13-16.
card_list_one = [[10,'10']]
card_list_two = [[6,'6'], [5,'5'], [4,'4'], [3,'3']]
test_string = """def test_{8:04d}_{0}{1}(self):
    hand = [Card({2}, '{3}', '{4}'),Card({5}, '{6}', '{7}')]
    do_dealer_turn(hand)
    
    self.assertEqual(len(hand), 3)
    """

for card_one in card_list_one:
    for card_two in card_list_two:
        iterator += 1
        print test_string.format(card_one[1], card_two[1], card_one[0], 'spades', card_one[1], card_two[0], 'spades', card_two[1], iterator)
        
# Check totals 17-21 (17 has no aces).
card_list_one = [[10,'10']]
card_list_two = [[11,'A'], [10,'10'], [9,'9'], [8,'8'], [7,'7']]
test_string = """def test_{8:04d}_{0}{1}(self):
    hand = [Card({2}, '{3}', '{4}'),Card({5}, '{6}', '{7}')]
    do_dealer_turn(hand)
    
    self.assertEqual(len(hand), 2)
    """

for card_one in card_list_one:
    for card_two in card_list_two:
        iterator += 1
        print test_string.format(card_one[1], card_two[1], card_one[0], 'spades', card_one[1], card_two[0], 'spades', card_two[1], iterator)
        
# Check totals 13-17 (with soft ace).
card_list_one = [[11,'A']]
card_list_two = [[6,'6'], [5,'5'], [4,'4'], [3,'3'], [2,'2']]
test_string = """def test_{8:04d}_{0}{1}(self):
    hand = [Card({2}, '{3}', '{4}'),Card({5}, '{6}', '{7}')]
    do_dealer_turn(hand)
    
    self.assertEqual(len(hand), 3)
    """

for card_one in card_list_one:
    for card_two in card_list_two:
        iterator += 1
        print test_string.format(card_one[1], card_two[1], card_one[0], 'spades', card_one[1], card_two[0], 'spades', card_two[1], iterator)
        
# Check totals 18-21 (with soft ace).
card_list_one = [[11,'A']]
card_list_two = [[10,'10'], [9,'9'], [8,'8'], [7,'7']]
test_string = """def test_{8:04d}_{0}{1}(self):
    hand = [Card({2}, '{3}', '{4}'),Card({5}, '{6}', '{7}')]
    do_dealer_turn(hand)
    
    self.assertEqual(len(hand), 2)
    """

for card_one in card_list_one:
    for card_two in card_list_two:
        iterator += 1
        print test_string.format(card_one[1], card_two[1], card_one[0], 'spades', card_one[1], card_two[0], 'spades', card_two[1], iterator)
        
# Check two soft aces.
card_list_one = [[11,'A']]
card_list_two = [[11,'A']]
test_string = """def test_{8:04d}_{0}{1}(self):
    hand = [Card({2}, '{3}', '{4}'),Card({5}, '{6}', '{7}')]
    do_dealer_turn(hand)
    
    soft_aces = 0
    
    if hand[0].isSoftAce():
        soft_aces += 1
        
    if hand[1].isSoftAce():
        soft_aces += 1
    
    self.assertEqual(len(hand), 2)
    self.assertEqual(soft_aces, 1) # Need to verify that two assertEquals are allowed.
    """

for card_one in card_list_one:
    for card_two in card_list_two:
        iterator += 1
        print test_string.format(card_one[1], card_two[1], card_one[0], 'spades', card_one[1], card_two[0], 'spades', card_two[1], iterator)