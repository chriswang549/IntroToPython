# Christopher Wang
# christwang
# 110969745
# CSE 101
# Homework #5

import random


class Card:
    suit_sym = {0: '\u2663', 1: '\u2666', 2: '\u2665', 3: '\u2660'}
    rank_sym = {0: '2', 1: '3', 2: '4', 3: '5', 4: '6', 5: '7', 6: '8',
                7: '9', 8: '10', 9: 'J', 10: 'Q', 11: 'K', 12: 'A'}

    def __init__(self, rank, suit):
        self.rank = rank
        self.suit = suit

    def __repr__(self):
        return self.rank_sym[self.rank] + self.suit_sym[self.suit]

    def __eq__(self, other):
        return self.suit == other.suit and self.rank == other.rank


class Player:
    def __init__(self, card_list):
        self.card_list = card_list
        self.score = 0

    def __repr__(self):
        return 'cards: ' + str(self.card_list) + ', score: ' + str(self.score)


# Utility function to help with testing. Don't change this function.
def build_deck():
    card_list = []
    for i in range(4):
        for j in range(13):
            card_list.append(Card(j, i))
    return card_list


# Utility function to help with testing. Don't change this function.
def build_players():
    player_list = []
    for i in range(4):
        player = Player([])
        player_list.append(player)
    return player_list


################ DO NOT MODIFY ANYTHING ABOVE THIS LINE ###################

# Part I
def deal_cards(player_list, card_list):
    return None


# Part II
def take_turn(current_suit, player):
    return None


# Part III
def round_winner(current_suit, cards_on_table):
    return None


# Part IV
def find_winner(player_list):
    return None


# Part V
def game_status(cards_on_table):
    return None


# This function will run the tests from the assignment PDF.
def run_tests():
    print('Part 1: deal_cards() test')
    card_list = build_deck()  # Able to build desk (10/100) #Script will get the cards and save it for later use
    random.shuffle(card_list)
    player_list = build_players()  # Able to build playersList (20/100)
    print('card_list: ' + str(card_list))
    deal_cards(player_list, card_list)  # Able to distributeCard (30/100) #Script will keep track of cards given to each player
    for i in range(len(player_list)):
        print('Cards dealt to player #' + str(i+1) + ': ' + str(player_list[i].card_list))

    print('\nPart 2: take_turn() test #1')
    card_list1 = [Card(0, 2), Card(0, 1), Card(1, 1), Card(2, 1), Card(3, 1), Card(4, 1)]
    print('Player\'s card_list before take_turn() function call: ' + str(card_list1))
    print('current_suit: ' + Card.suit_sym[0])
    card = take_turn(0, Player(card_list1))
    print('Player\'s card_list after take_turn() function call:  ' + str(card_list1))
    print('Returned card: ' + str(card))

    print('\nPart 2: take_turn() test #2')
    card_list2 = [Card(0, 1), Card(1, 1), Card(2, 1), Card(3, 1), Card(4, 1), Card(4, 2)]
    print('Player\'s card_list before take_turn() function call: ' + str(card_list2))
    print('current_suit: None')
    card = take_turn(None, Player(card_list2))
    print('Player\'s card_list after take_turn() function call:  ' + str(card_list2))
    print('Returned card: ' + str(card))

    print('\nPart 2: take_turn() test #3')
    card_list3 = [Card(0, 2), Card(0, 1), Card(1, 1), Card(7, 1), Card(3, 1), Card(4, 1)]
    print('Player\'s card_list before take_turn() function call: ' + str(card_list3))
    print('current_suit: ' + Card.suit_sym[1])
    card = take_turn(1, Player(card_list3))
    print('Player\'s card_list after take_turn() function call:  ' + str(card_list3))
    print('Returned card: ' + str(card))

    print('\nPart 3: round_winner() test #1')
    card_list1 = [Card(0, 2), Card(1, 2), Card(2, 2), Card(3, 2)]
    print('cards_on_table: ' + str(card_list1))
    print('current_suit:   ' + Card.suit_sym[2])
    winner = round_winner(2, card_list1)
    print('Winner: Player #' + str(winner))

    print('\nPart 3: round_winner() test #2')
    card_list2 = [Card(0, 1), Card(1, 1), Card(2, 1), Card(3, 2)]
    print('cards_on_table: ' + str(card_list2))
    print('current_suit:   ' + Card.suit_sym[1])
    winner = round_winner(1, card_list2)
    print('Winner: Player #' + str(winner))

    print('\nPart 3: round_winner() test #3')
    card_list3 = [Card(0, 3), Card(1, 1), Card(2, 1), Card(3, 2)]
    print('cards_on_table: ' + str(card_list3))
    print('current_suit:   ' + Card.suit_sym[3])
    winner = round_winner(3, card_list3)
    print('Winner: Player #' + str(winner))

    print('\nPart 4: find_winner() test #1')
    player_list[0].score = 10
    player_list[1].score = 1
    player_list[2].score = 1
    player_list[3].score = 1
    print('Player scores:', player_list[0].score, player_list[1].score, player_list[2].score, player_list[3].score)
    winner = find_winner(player_list)  # Obvious winner
    print('Winner(s):', winner)

    print('\nPart 4: find_winner() test #2')
    player_list[0].score = 8
    player_list[1].score = 2
    player_list[2].score = 2
    player_list[3].score = 1
    winner = find_winner(player_list)  # 2 winners
    print('Player scores:', player_list[0].score, player_list[1].score, player_list[2].score, player_list[3].score)
    winner = find_winner(player_list)  # Obvious winner
    print('Winner(s):', winner)

    print('\nPart 4: find_winner() test #3')
    player_list[0].score = 4
    player_list[1].score = 4
    player_list[2].score = 4
    player_list[3].score = 1
    winner = find_winner(player_list)  # 2 winners
    print('Player scores:', player_list[0].score, player_list[1].score, player_list[2].score, player_list[3].score)
    winner = find_winner(player_list)  # Obvious winner
    print('Winner(s):', winner)

    print('\nPart 5: game_status() test #1')
    card_list1 = [Card(0, 2), Card(0, 3), Card(0, 0), Card(0, 1)]
    print('cards_on_table:', card_list1)
    current_state = game_status(card_list1)  # all same rank
    print('Returned string:')
    print(current_state)

    print('Part 5: game_status() test #2')
    card_list2 = [Card(0, 2), Card(1, 2), Card(3, 2), Card(12, 2)]
    print('cards_on_table:', card_list2)
    current_state = game_status(card_list2)  # all same suit
    print('Returned string:')
    print(current_state)

    print('Part 5: game_status() test #3')
    card_list3 = [Card(2, 1), Card(1, 2), Card(12, 2), Card(10, 3)]
    print('cards_on_table:', card_list3)
    current_state = game_status(card_list3)  # Totally random
    print('Returned string:')
    print(current_state)


# This function will simulate a game of Bridge with 4 computer players.
def simulate_game():
    deck = build_deck()
    random.shuffle(deck)
    players = build_players()
    deal_cards(players, deck)
    for i in range(13):
        print('\nRound #' + str(i+1))
        current_suit = random.choice(random.choice(players).card_list).suit
        print('Suit: ' + Card.suit_sym[current_suit])
        cards_on_table = []
        for p in players:
            card = take_turn(current_suit, p)
            cards_on_table.append(card)
        print(game_status(cards_on_table).strip())
        rwinner = round_winner(current_suit, cards_on_table)
        print('Round winner: Player #' + str(rwinner))
        players[rwinner-1].score += 1
        scores = [str(p.score) for p in players]
        print('Player scores: ' + ' '.join(scores))
    gwinner = find_winner(players)
    print('Game winner(s):', gwinner)


if __name__ == '__main__':
    run_tests()
    #simulate_game()
