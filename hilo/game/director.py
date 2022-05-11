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
        self.points = 300
        self.score = 300
        self.continue_playing = True

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


    def get_inputs(self):
        """Ask the user if they want to pick another card.
        
        Args:
            self (Director): An instance of Director.
        """
        get_card = input("Pick a card? [y/n] ")
        self.continue_playing = (get_card == "y")

    def do_updates(self):
        """Updates the player's score.
        
        Args:
            self (Director): An instance of Director.
        """
        if not self.continue_playing:
            return

        #for i in range(len(self.))
    
    def display_card(self):
        """
        this 
        """
    

       drawn_card = self.deck.draw()
       print(drawn_card)

        

    def players_choice():
        pass


    def get_next_card():
        pass

    def calculate_score(self):
        # self.score
        pass

    def play_again(self): #I'll take a shot at this one - Matt
        
        if self.score <= 0:
            self.continue_playing = False
            return print(f'Your score is 0. Game over.')
            