import random

class CoinFlipGame:
    def __init__(self):
        self.user_choice = None
        self.coin_flip = None
        
    def get_user_choice(self):
        self.user_choice = input("Enter your choice (head/tail): ").lower()
        while self.user_choice not in ['head', 'tail']:
            print("Invalid choice. Please enter 'head' or 'tail'.")
            self.user_choice = input("Enter your choice (head/tail): ").lower()
    
    def flip_coin(self):
        self.coin_flip = random.choice(['head', 'tail'])
    
    def display_result(self):
        print(f"The coin landed on: {self.coin_flip}")
        
        if self.user_choice == self.coin_flip:
            print("Congratulations! You guessed correctly.")
        else:
            print("Sorry, you guessed incorrectly.")
    
    def play(self):
        self.get_user_choice()
        self.flip_coin()
        self.display_result()

# Usage
# game = CoinFlipGame()
# game.play()

def main():
    print("Welcome to the Coin Flip Game!")
    while True:
        game = CoinFlipGame()
        game.play()
        
        play_again = input("Do you want to play again? (yes/no): ").lower()
        if play_again not in ['yes', 'y']:
            print("Thank you for playing! Goodbye!")
            break

if __name__ == "__main__":
    main()