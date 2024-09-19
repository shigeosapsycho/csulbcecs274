from MobileCritter import MobileCritter
from Insect import Insect
 
 
class Spider(Insect, MobileCritter):
    def __init__(self):
        Insect.__init__(self)
        self.x = 0
        self.y = 0
 
    def move_right(self):
        """moves this spider's position 1 unit right"""
        # todo
        MobileCritter.move_right(self)
 
    def move_left(self):
        """moves this spider's position 2 units left"""
        # todo
        MobileCritter.move_left(self)
 
    def move_up(self):
        """moves this spider's position 1 unit up"""
        # todo
        MobileCritter.move_up(self)
 
    def move_down(self):
        """moves this spider's position 2 units down"""
        # todo
        MobileCritter.move_down(self)
 
    def __str__(self):
        return u'\u1F577'