from MobileCritter import MobileCritter
from Insect import Insect
 
 
class Ant(Insect, MobileCritter):
 
    def __init__(self):
        Insect.__init__(self)
        self.x = 0
        self.y = 0
 
    def move_right(self):
        """moves this ant's position 1 unit right"""
        # todo
        self.position[0] += 1
 
    def move_left(self):
        """moves this ant's position 1 unit right"""
        # todo
        self.position[0] -= 1
 
    def move_up(self):
        """moves this ant's position 2 units up"""
        # todo
        self.position[1] += 2
 
    def move_down(self):
        """moves this ant's position 2 units down"""
        # todo
        self.position[1] -= 2
 
    def __str__(self):
        return u'\u1F41C'
