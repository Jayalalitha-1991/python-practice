import random

class CoinFlipGame:
    def __init__(self):
        self.user_choice = None
        self.coin_flip = None
        
    def get_user_choice(self, choice):
        self.user_choice = choice.lower()
    
    def flip_coin(self):
        self.coin_flip = random.choice(['head', 'tail'])
    
    def get_result(self):
        return self.coin_flip == self.user_choice
