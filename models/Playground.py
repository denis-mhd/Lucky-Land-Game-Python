from models.Cell import Cell
from models.CardFactory import *

class Playground():

    def __init__(self, size):
        self.size = size

    def build_playground(self):
        field = []      
        count = 0
        for i in range(0, self.size):
            row = []
            cards = get_cards()
            for j in range(0, self.size):
                if j % 2 == 0:
                    random.shuffle(cards)
                cell = Cell(i,j,cards)                  
                count += 1
                row.append({count: cell})            
            field.append(row)       
        return field                
                
   
      
        
        

                          


