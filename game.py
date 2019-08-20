
import random

suits = ('Hearts', 'Diamonds', 'Spades', 'Clubs')
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
        return self.rank + " of " + self.suit


class Deck:

    def __init__(self):     # Deck initialization
        self.deck = []      # Initialize an empty list
        for suit in suits:      # loop over suit and rank in lists: suits & ranks
            for rank in ranks:
                # add one card to the Deck
                self.deck.append(Card(suit, rank))

    def __str__(self):      # String Method to display the Player's Deck
        game_deck = ''        # Initialize Deck changes each round it starts with empty String
        for card in self.deck:      # Loop over Class Card in Class Deck
            game_deck += '\n' + card.__str__()        # Add String to print Players cards
        return 'Your Cards are: ' + game_deck

    def shuffle(self):
        random.shuffle(self.deck)   # Shuffles the entre carddeck

    def deal(self):
        # Deals cards and removes one single card at the end of the random deck-list
        player_card = self.deck.pop()
        return player_card


# test_deck = Deck()
# print(test_deck)


class Hand:

    def __init__(self):     # Initializes a Hand with an empty cards list; Sets values and aces in this list as 0
        self.cards = []
        self.value = 0
        self.aces = 0

    def add_card(self, card):
        # When a card is added to a Hand, the Value of this hand is calculated with the Dictionary values[key, value]
        self.cards.append(card)
        self.value += values[card.rank]

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


def take_bet(chips):
    while True:
        try:
            chips.bet = int(input("How many chips do you want to bet?: "))
        except ValueError:
            print("Please enter an integer.")
        else:
            if chips.bet > chips.total:
                print("100 is the maximum amount of Chips one can bet.")
            else:
                break
# def take_bet(chips):     # Betting action initialized
    # while chips.bet >= 1:        # Player can only bet if chipcount >=1
    #    try:
    #        # Player input as integer
    #        int(input("How many chips do you want to bet?"))
    #    except:     # Exception Handling in case of wrong user input
    #        print("Please insert a number")
    #    else:
    #        if chips.bet > chips.total:     # If the amount of chips bet is higher the amount of total chips of the players stack, bet-action is denied
    #            print("You dont have enough chips to make that move")
    #        else:
    #            break       # Leaves the loop immediately when if-statement is true


def hit(deck, hand):
    # one single card is dealt from the deck and added to the hand // Game-Action
    hand.add_card(deck.deal())
    # method to adjust hands value in case of aces in players hands > 21
    # hand.adjust_for_ace()


def hit_or_stand(deck, hand):
    global playing      # Global variable since it is crucial for Main-Game functionality True = play, FALSE = no play
    # As long as playing is true, the Player can choose either between getting another card (hit) or standing and leave his deck unchanged
    while True:
        i = input("Press 'h' for Hit or 's' for Stand: ")

        if i[0].lower() == 'h':
            hit(deck, hand)

        elif i[0].lower() == 's':
            playing = False

        else:
            print("Please enter 'h' or 's'")
            continue        # Interrupts Selection Menu if something is entered except of "h" or "s"
        break       # Leaves loop after conditions are passed succesfully


# Functions to show/hide cards and deal with different game scenarios

def show_some(player, dealer):        # Function for Dealer and Player to display their Hands
    # One card to be hidden, second card (Index[1]) to be displayed
    print("Dealer's Hand: ")
    print("***************")
    print(dealer.cards[1])
    print()
    print("\nPlayer's Hand: ", *player.cards, sep='\n')
    print()
    #print(player.cards[0], player.cards[1])


def show_all(player, dealer):
    # Reveal of Dealers cards (cards list is creating in Hand class)
    print("\nDealer's Hand: ", *dealer.cards, sep='\n')
    print("Dealer's Hand: ", dealer.value)      # Including values
    print()
    # Reveal of players cards
    print("\nPlayer's Hand: ", *player.cards, sep='\n')
    print("Player's Hand: ", player.value)      # Including value
    print()

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
while True:
    # Print an opening Statement
    print("Welcome to Johnny Knoxville, this is Blackjack")
    print()

    # Create and shuffle a Deck, deal two cards to the player
    deck = Deck()
    deck.shuffle()

    player_hand = Hand()
    player_hand.add_card(deck.deal())
    player_hand.add_card(deck.deal())

    dealer_hand = Hand()
    dealer_hand.add_card(deck.deal())
    dealer_hand.add_card(deck.deal())

    # Set up the Player's chips (100 default)
    player_chips = Chips()

    # Prompt the player for their first bet
    take_bet(player_chips)

    # Show cards, but keep one dealer card hidden
    show_some(player_hand, dealer_hand)

    while playing:

        hit_or_stand(deck, player_hand)

        show_some(player_hand, dealer_hand)

        if player_hand.value > 21:
            player_busts(player_hand, dealer_hand, player_chips)
            break

    if player_hand.value <= 21:
        while dealer_hand.value < 17:
            hit(deck, dealer_hand)

        show_all(player_hand, dealer_hand)

        if dealer_hand.value > 21:
            dealer_busts(player_hand, dealer_hand, player_chips)

        elif dealer_hand.value > player_hand.value:
            dealer_wins(player_hand, dealer_hand, player_chips)

        elif dealer_hand.value < player_hand.value:
            player_wins(player_hand, dealer_hand, player_chips)

        else:
            push(player_hand, dealer_hand)

    print('This is your current amount of chips: ', player_chips.total)

    play_again = input(
        "Wanna loose more money? Press 'c' to continue or 'l' to leave.")

    if play_again[0].lower() == 'c':
        playing = True
        continue
    else:
        print("Game Over")
        break
