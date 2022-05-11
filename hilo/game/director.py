from game.card import Card
from game.deck import Deck


class Director:

    """
    An instance that directs the card game

    The responsibility of a director is to control the sequence of play and terminate game when 
    player no longer wants to play.

    Attributes:

        continue_playing (boolean): whether or not the game is being played.
        
        score (int) : The score for current round
        points (int): The current score for the entire game
        deck 

    """


    def __init__(self):
        """
        Constructs a new Director

        Args:
            self (Director)

        """
        self.deck = Deck()
        self.deck.shuffle() #shuffle the deck before we use it
        self.score = 300
        self.continue_playing = True
        self.first_card = None
        self.second_card = None
        self.players_choice = None

    def start_game(self):

        """
        Starts the game by running the main loop

        Args:
        self(Director): an instance of Director.

        """
        while self.continue_playing:
            self.display_card()
            self.get_player_choice()
            self.get_next_card()
            self.calculate_score()
            self.play_again()
    
    def display_card(self):
        """
        this will draw a card from deck and store it for score calculations
        it will then displauy the card

        """
        
        self.first_card = self.deck.draw()
        print(f"The Card is : {self.first_card}")

    def get_player_choice(self):
        # take, validate, store.
        while True:
            self.player_choice = input("Higher or Lower? [h/l] ").lower()
            if self.player_choice == "h" or self.player_choice == "l":
                break
            else:
                print("Please enter an h or l to continue...")
                



    def get_next_card(self):
         """
        this will draw a card from deck and store it for score calculations
        it will then displauy the card

        """
        
         self.second_card = self.deck.draw()
         print(f"Next card was: {self.first_card}")
        

    def calculate_score(self):
        # Dylan worked here :)
        # still need to do math and logic here
        first_card_numerical = self.deck.values.index(self.first_card.value)
        second_card_numerical = self.deck.values.index(self.second_card.value)
        if first_card_numerical == 0:
            # If card is ace
            first_card_numerical = 100
            # aces high (wasn't sure the numerical value king would have, so overshot it by intention)

        if second_card_numerical == 0:
            # see if-statement above this one
            second_card_numerical = 100

        # if both cards are equal, counts as higher
        second_card_is_higher = second_card_numerical >= first_card_numerical
        

        print(f"Your score is: {self.score}")

    def play_again(self): #I'll take a shot at this one - Matt
        
        while self.score <= 0:
           
            answer = input(f"GAME OVER. Your score has reached 0. Would you like to play again [y/n]?")
            if answer == "y":
                 return self.start_game()
            elif answer == "n":
                self.continue_playing = False
                print("Thanks for playing!")
            else:
                print("Please enter y or n.")
            
            
            #answer = None 
            #while answer not in ("y", "n"): 
               #answer = input("Enter y or n:") 
                #if answer == "y":
                   # return start_game()
               #elif answer == "n": 
                    #return self.continue_playing = False
               #else: 
        	        #print("Please enter y or n.") 
            
            #self.continue_playing = False
            #return print(f'Your score is 0. Game over.')
