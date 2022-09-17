import random


class GameSpock:
    # Class attributes
    user_win_message: str = "You win!"
    computer_win_message: str = "Computer wins!"
    draw_message: str = "It's a draw!"
    figures: str = 'scissorspaperrocklizardSpockscissorslizardpaperSpockrockscissors'  # Winning combinations

    def __init__(self, user_choice: str = None, random_program_choice: str = None):
        self.user_choice: str = user_choice
        self.random_program_choice: str = random_program_choice

    @staticmethod
    def rules():
        print("HERE ARE THE RULES OF THE GAME: \n"
              "Scissors cuts paper, paper covers rock, rock crushes lizard,\n"
              "lizard poisons Spock, Spock smashes scissors,"
              "scissors decapitates lizard,\nlizard eats paper,"
              "paper disproves Spock, Spock vaporizes rock,\n"
              "and as it always has, rock crushes scissors.\n\n")

    def user_input(self) -> str:  # Entering player data and checking it
        while True:
            print("Please, make your choice: rock, paper, scissors, lizard or Spock? To interrupt the game enter ")
            self.user_choice = input("Your choice: ").lower()
            if self.user_choice in ["rock", "paper", "scissors", "lizard", "spock"]:
                return self.user_choice
            else:
                print("Please make correct input.")

    def program_choice(self):  # Selection of a computer by random
        choices_list = ["rock", "paper", "scissors", "lizard", "spock"]
        self.random_program_choice: str = random.choice(choices_list)
        print(f"Computer: {self.random_program_choice}")

    def winner_detector(self) -> str:  # Selection of the winner
        if self.user_choice == self.random_program_choice:
            return GameSpock.draw_message
        elif str(self.user_choice) + str(self.random_program_choice) in GameSpock.figures:
            return GameSpock.user_win_message
        else:
            return GameSpock.computer_win_message

    def main(self):  # Collection of all functions together
        while True:
            GameSpock.rules()
            GameSpock.user_input(self)
            GameSpock.program_choice(self)
            print(GameSpock.winner_detector(self))
            play_again = input("Play again? (Y/N)").lower()
            if play_again == "y":
                continue
            else:
                break


if __name__ == "__main__":
    first = GameSpock()
    first.main()
