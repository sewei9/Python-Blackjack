import random

suits = ('Hearts', 'Diamnods', 'Spades', 'Clubs')
ranks = ('Two', 'Three', 'Four', 'Five', 'Six', 'Seven',
         'Eight', 'Nine', 'Ten', 'Jack', 'Queen', 'King', 'Ace')
values = {'Two': 2, 'Three': 3, 'Four': 4, 'Five': 5, 'Six': 6, 'Seven': 7, 'Eight': 8, 'Nine': 9, 'Ten': 10, 'Jack': 10,
          'Queen': 10, 'King': 10, 'Ace': 11}

playing = True


class Card:

    def __init__(self, suit, rank):
        self.suit = suit
        self.rank = rank

    def __str__(self):
        return self.rank + "of" + self.suit


class Deck:

    def __init__(self):
        self.deck = []
        for suit in suits:
            for rank in ranks:
                self.deck.append(Card(suit, rank))

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


test_deck = Deck()
print(test_deck)


class Hand:

    def __init__(self):
        self.cards = []
        self.value = 0
        self.aces = 0

    def add_card(self, card):
        self.cards.append(card)
        self.values += values[card.rank]

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

    # def tie_bet(self):


def take_bet():
    while chips.bet > 1:
        try:
            int(input("How many chips do you want to bet?"))
        except:
            print("Please insert a number(int)")
        else:
            if chips.bet > chips.total:
                print("You dont have enough chips to make that move")
            else:
                break


def hit(deck, hand):
    hand.add_card(deck.deal)
    hand.adjust_for_ace()


def hit_or_stand(deck, hand):
    global playing
    while True:
        i = input("Press 'h' for Hit or 's' for Stand")
        if i == "h":
            hit(deck, hand)
        elif i == "s":
            playing = False
        else:
            print("Please enter 'h' or 's'")
            continue
        break


# Functions to show/hide cards and deal with different game scenarios

def show_some(play, dealer):
    print("Dealer cards: Hidden Card", "\n", dealer.cards[1])
    print("Player cards: ", player.cards[0], "\n", player.cards[1])


def show_all(player, dealer):
    print("Dealer cards: ", dealer.cards[0], "\n", dealer.cards[1])
    print("Dealer's Hand: ", dealer.value)

    print("Player cards: ", player.cards[0], "\n", player.card[1])
    print("Player's Hand: ", player.value)


# Player/Dealer wins/losses or ties the bet

def player_busts(dealer, player, chips):
    print("Busted!")
    chips.lose_bet()


def player_wins(dealer, player, chips):
    print("Win!")
    chips.win_bet()


def dealer_busts(dealer, player, chips):
    print("Dealer busts!")
    chips.win_bet()


def dealer_wins(dealer, player, chips):
    print("Dealer wins!")
    chips.lose_bet()

# Dealer and Player tie for win. Bet will be returned to player
def push(dealer, player):    
    print("It's a tie") 


# Main Game
