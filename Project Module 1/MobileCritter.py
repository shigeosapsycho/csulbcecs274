class MobileCritter:

    def move_right(self):
        self.position[0] += 1

    def move_left(self):
        self.position[0] -= 1
    def move_up(self):
        self.position[1] += 1
        
    def move_down(self):
        self.position[1] -= 1