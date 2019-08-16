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

    def __init__(self):     # Deck initialization
        self.deck = []      # Initialize an empty list
        for suit in suits:      # loop over suit and rank in lists: suits & ranks
            for rank in ranks:
                self.deck.append(Card(suit, rank))      # add one card to the Deck

    def __str__(self):      # String Method to display the Player's Deck
        player_deck = ''        # Initialize Deck changes each round it starts with empty String
        for Card in self.deck:      # Loop over Class Card in Class Deck
            player_deck + Card.__str__()        # Add String to print Players cards
        return 'Your Cards are: ' + player_deck

    def shuffle(self):
        random.shuffle(self.deck)   # Shuffles the entre carddeck

    def deal(self):
        player_card = self.deck.pop()       # Deals cards and removes one single card at the end of the random deck-list
        return player_card


test_deck = Deck()
print(test_deck)


class Hand:

    def __init__(self):     # Initializes a Hand with an empty cards list; Sets values and aces in this list as 0
        self.cards = []
        self.value = 0
        self.aces = 0

    def add_card(self, card):
        self.cards.append(card)     # When a card is added to a Hand, the Value of this hand is calculated with the Dictionary values[key, value]
        self.values += values[card.rank]

    def adjust_for_ace(self):
        pass


class Chips:

    def __init__(self):     # Chip stack initialization
        self.total = 100
        self.bet = 0

    def win_bet(self):      # Chips added to total_chips_amount if bet is won
        self.total += self.bet

    def lose_bet(self):     # CHips removed from total_chips_amount if bet is lost
        self.total -= self.bet

    # def tie_bet(self):        Chips are lead back to player in case of push/tie


def take_bet():     # Betting action initialized
    while chips.bet >= 1:        # Player can only bet if chipcount >=1
        try:
            int(input("How many chips do you want to bet?"))        # Player input as integer
        except:     # Exception Handling in case of wrong user input
            print("Please insert a number")
        else:
            if chips.bet > chips.total:     # If the amount of chips bet is higher the amount of total chips of the players stack, bet-action is denied
                print("You dont have enough chips to make that move")
            else:
                break       # Leaves the loop immediately when if-statement is true


def hit(deck, hand):
    hand.add_card(deck.deal)        # one single card is dealt from the deck and added to the hand // Game-Action
    hand.adjust_for_ace()       # method to adjust hands value in case of aces in players hands > 21


def hit_or_stand(deck, hand):
    global playing      # Global variable since it is crucial for Main-Game functionality True = play, FALSE = no play
    while True:     # As long as playing is true, the Player can choose either between getting another card (hit) or standing and leave his deck unchanged
        i = input("Press 'h' for Hit or 's' for Stand")
        if i == "h":
            hit(deck, hand)
        elif i == "s":
            playing = False
        else:
            print("Please enter 'h' or 's'")
            continue        # Interrupts Selection Menu if something is entered except of "h" or "s"
        break       # Leaves loop after conditions are passed succesfully


# Functions to show/hide cards and deal with different game scenarios

def show_some(play, dealer):        # Function for Dealer and Player to display their Hands
    print("Dealer cards: Hidden Card", "\n", dealer.cards[1])       # One card to be hidden, second card (Index[1]) to be displayed
    print("Player cards: ", player.cards[0], "\n", player.cards[1])     # Fo Players Hand both cards (Index[0],[1]) are visible


def show_all(player, dealer):
    print("Dealer cards: ", dealer.cards[0], "\n", dealer.cards[1])     # Reveal of Dealers cards (cards list is creating in Hand class)
    print("Dealer's Hand: ", dealer.value)      # Including values

    print("Player cards: ", player.cards[0], "\n", player.card[1])      # Reveal of players cards
    print("Player's Hand: ", player.value)      # Including value


# Player/Dealer wins/losses or ties the bet

def player_busts(dealer, player, chips):
    print("Busted!")
    chips.lose_bet()        # lose_bet function is part of Class Chips


def player_wins(dealer, player, chips):
    print("Win!")
    chips.win_bet()     # win_bet is part of Class Chips


def dealer_busts(dealer, player, chips):
    print("Dealer busts!")
    chips.win_bet()     


def dealer_wins(dealer, player, chips):
    print("Dealer wins!")
    chips.lose_bet()

# Dealer and Player tie for win. Bet will be returned to player
def push(dealer, player):       # No particular action since chips stack stays untouched
    print("It's a tie") 


# Main Game
