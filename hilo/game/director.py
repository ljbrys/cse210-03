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
        playing_deck = Deck()
        """
        this will draw a card from deck and store it for score calculations
        it will then displauy the card

        """
        
        drawn_card = self.deck.draw()
        print(drawn_card)

    

       
        

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
        
        pass

    def play_again(self): #I'll take a shot at this one - Matt
        
        if self.score <= 0:
            self.continue_playing = False
            return print(f'Your score is 0. Game over.')