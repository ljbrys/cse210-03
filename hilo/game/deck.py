from game.card import Card
import random

class Deck:
    def __init__(self, values = ["Ace","2","3","4","5","6","7","8","9","10","Jack","Queen","King"], suits = ["Spades","Hearts","Clubs","Diamonds"]):
        self.cards = []        
        self.paramaters.values = values
        self.parameters.suits = suits
        self.fill()

    def shuffle(self):
        random.shuffle(self.cards)

    def draw(self):
        return self.cards.pop()

    def fill(self):        
        for i in range(len(self.paramaters.suits)):
            for j in range(len(self.paramaters.values)):
                self.cards.append(Card(self.paramaters.values[j],self.paramaters.suits[i]))

    def deck_check(self):
        print(self.cards)