import random

### Use this import in the final version
# from game.card import Card

### Use this import for testing
from card import Card


class Deck:
    # """A deck of playing cards
    #
    # The responsibility of Deck is to manage and keep track of the types and identities of cards as
    #     well as their location within the deck, as well as the cards that have already been used.
    #
    # Attributes:
    #     cards (list):         A list to contain multiple card objects that are currently in the
    #                               Deck
    #     drawn_cards (list):   A list to contain multiple card objects that have been drawn from
    #                               the deck
    #     values (list):        A list of all face values present in this type of deck.
    #     suits (list):         A list of all suit identities present in this type of deck.
    # """
    def __init__(self, values: list = ["Ace","2","3","4","5","6","7","8","9","10","Jack","Queen","King"], suits: list = ["Spades","Hearts","Clubs","Diamonds"]):
        # """Constructs a new instance of Deck
        #
        # Takes optional 'values' and 'suits' arguments to define the structure of the deck (in case
        #     this class is used for types of playing cards other than the traditional Western-52.
        #
        # Args:
        #     self (Deck):      An instance of Deck.
        #     values (list):    A list of potential face values of cards.
        #     suits (list):     A list of potential suit identities of cards.
        # """
        self.cards = []
        self.drawn_cards = []

        self.values = values
        self.suits = suits

        for i in range(len(self.suits)):
            for j in range(len(self.values)):
                self.cards.append(Card(self.values[j],self.suits[i]))
        

    def shuffle(self):
        # """Shuffles the cards that are currently in the deck
        #
        # Args:
        #     self (Deck):      An instance of Deck.
        # """
        random.shuffle(self.cards)

    def draw(self):
        # """Draws a card from the deck and places it into the drawn_cards list
        # 
        # Args:
        #     self (Deck):      An instance of Deck
        # """
        drawn_card = self.cards.pop()
        self.drawn_cards.append(drawn_card)
        return drawn_card

    def fill(self):
        # """Moves cards from the drawn_cards list back into the current deck
        # 
        # Args:
        #     self (Deck):      An instance of Deck
        # """
        for i in range(len(self.drawn_cards)):
            self.cards.append(self.drawn_cards.pop())

    def deck_check(self):
        # just here as a debug tool to optionally see the state of the cards in the deck at any given time
        print(*self.cards)