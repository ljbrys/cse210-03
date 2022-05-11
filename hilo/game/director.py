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
            self.players_choice()
            self.get_next_card()
            self.calculate_score()
            self.play_again()
    
    def display_card(self):
        """
        this will draw a card from deck and store it for score calculations
        it will then displauy the card

        """

        self.first_card = self.deck.draw()
        print(self.first_card)

    def players_choice():
        # player_choice = int(input("Higher or Lower?"))
        # if player_choice == "h".lower():
        #     print("Higher")
        # elif player_choice == "l".lower():
        #     print("Lower!")
        pass


    def get_next_card(self):
        pass

    def calculate_score(self):
        # self.
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