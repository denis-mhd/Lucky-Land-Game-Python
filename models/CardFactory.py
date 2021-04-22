import models.Player
import random
from abc import ABC, abstractmethod

class _Card(ABC):
    @abstractmethod
    def action():
        pass

        
class GoodCard(_Card):
    health_points = 50

    def __init__(self):
        self.health_points = 50
        

    def action(self, player):
        player.add_health(self.health_points)


class BadCard(_Card):
    damage = 10

    def __init__(self):
        self.damage = 10

    def action(self, player):
        player.take_damage(self.damage)
    

class TripCard(_Card):

    def __init__(self):
        pass
        

    def action(self, player):
        player.move()   


def get_cards():
    cards = [GoodCard(), BadCard(), TripCard()]
    return cards