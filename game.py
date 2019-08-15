import random

suits = ('Hearts', 'Diamnods', 'Spades', 'Clubs')
ranks = ('Two', 'Three', 'Four', 'Five', 'Six', 'Seven', 'Eight', 'Nine', 'Ten', 'Jack', 'Queen', 'King', 'Ace')
values = {'Two':2, 'Three':3, 'Four':4, 'Five':5, 'Six':6, 'Seven':7, 'Eight':8, 'Nine':9, 'Ten':10, 'Jack':10, 
            'Queen':10, 'King':10, 'Ace':11}

playing = True

class Card:

    def __init__(self, suit, rank):
        self.suit = suit
        self.rank = rank

    def __str__(self):
        return self.suit + "of" + self.rank  


class Deck:

    def __init__(self):
        self.deck = []
        for suit in suits:
            for rank in ranks:
                self.deck.append(Card(suit,rank))

    def __str__(self):
        player_deck = ''
        for Card in self.deck:
            player_deck + Card.__str__()
        return 'Your Cards are: ' + player_deck


    def shuffle(self):
        random.shuffle(self.deck)

    def deal(self):
        player_card = self.card.pop()
        return player_card


class Hand:

    def __init__(self):
        self.cards = []
        self.value = 0
        self.aces = 0


    def add_card(self, card):
        self.cards.append(card)
        self.values 


    def adjust_for_ace(self):
        pass


class Chips:

    def __init__(self):
        self.total = 100
        self.bet = 0


    def win_bet(self):
        self.total += self.bet


    def lose_bet(self):
        self.total -= self.bet

test_deck = Deck()
print(test_deck)

