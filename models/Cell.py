from models.CardFactory import *

class Cell:

    def __init__(self, row, col, cards):
        self.row = row
        self.col = col
        self.cards = cards
      
  
    def card_shuffle(cards):
        random.shuffle(cards)
        return cards
                