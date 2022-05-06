class Card:
    # """A playing card

    # The responsibility of Card is to represent a single playing card
    #     and also contain its properties (face value, suit, and printable identity)
    
    # Attributes:
    #     value (str): The face value of the card. for traditional western playing cards, this would
    #         be 'Ace', '2', '10', 'King', etc.
    #     suit (str): The suit attached to the card's identity, such as "spades", "hearts", "clubs",
    #         and "diamonds".
    # """
    def __init__(self, value: str = "", suit: str = "") -> None:
        # """Constructs a new instance of Card with a value and suit attribute.
        
        # Args:
        #     self (Card): An instance of Card.
        #     value (str): A name for the face value of the card
        #     suit (str): A name for the suit identity of the card
        # """
        self.value = value
        self.suit = suit

    def __str__(self):
        # """Defines the behavior of 'str(instance_of_Card)'

        # Args:
        #     self (Card): An instance of card
        # """
        return f"{self.value} of {self.suit}"