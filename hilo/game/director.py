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

    def start_game(self):

        """
        Starts the game by running the main loop

        Args:
        self(Director): an instance of Director.

        """
        self.deck = Deck()
        while True:
            self.deck.fill()
            self.deck.shuffle()
            self.score = 300
            self.continue_current_round = True
            self.continue_to_new_round = True
            while self.continue_current_round:
                self.display_card()
                self.get_player_choice()
                self.get_next_card()
                self.calculate_score()
                self.play_again()
            if not self.continue_to_new_round:
                break
    
    def display_card(self):
        """
        this will draw a card from deck and store it for score calculations
        it will then displauy the card

        """
        
        if len(self.deck.cards) < 2:
            self.deck.fill()
            self.deck.shuffle()

        self.first_card = self.deck.draw()
        print(f"\nThe Card is: {self.first_card}")

    def get_player_choice(self):
        # take, validate, store.
        while True:
            self.player_guess = input("Higher or Lower? [h/l] ").lower()
            if self.player_guess == "h" or self.player_guess == 'l':
                break
            else:
                print("Invalid answer, please enter an h or an l.")
                



    def get_next_card(self):
         """
        this will draw a card from deck and store it for score calculations
        it will then displauy the card

        """
        
         self.second_card = self.deck.draw()
         print(f"Next card was: {self.second_card}")
        

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

        player_guessed_hi = None
        if self.player_guess == 'h':
            player_guessed_hi = True
        elif self.player_guess == 'l':
            player_guessed_hi = False

        if second_card_is_higher == player_guessed_hi:
            self.score += 100
        else:
            self.score -= 75        

        print(f"Your score is: {self.score}")

    def play_again(self): #I'll take a shot at this one - Matt
            
            
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
        
        if self.score <= 0:
            self.continue_current_round = False
            print("GAME OVER. Your score has reached 0.")
        else:
            while True:
                player_plays_again = input("Play again? [y/n] ").lower()
                if player_plays_again == 'y':
                    break
                elif player_plays_again == 'n':
                    print("GAME OVER. Thanks for playing.")
                    self.continue_current_round = False
                    break
                else:
                    print("Invalid answer, please enter a y or an n.")

        while not self.continue_current_round:
            self.continue_to_new_round = input("Would you like to start a new round [y/n]? ").lower()
            if self.continue_to_new_round == 'y':
                break
            elif self.continue_to_new_round == 'n':
                self.continue_to_new_round = False
                break
            else:
                print("Invalid answer, please enter a y or an n.")
        