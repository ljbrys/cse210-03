class Director:
    """
    An instance that directs the card game

    The responsibility of a director is to control the sequence of play and terminate game when 
    player no longer wants to play.

    Attributes:

        continue_playing (boolean): whether or not the game is being played.
        
        score (int) : The score for current round
        points (int): The current score for the entire game

    """


    def __init__(self):
        """
        Constructs a new Director

        Args:
            self (Director)
        """
        self.points = 300
        self.continue_playing = True
        self.score = 0



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
        # this is a test Larry J. Brys
        pass

    def players_choice():
        pass


    def get_next_card():
        pass

    def calculate_score():
        pass

    def play_again():
        pass

test test test