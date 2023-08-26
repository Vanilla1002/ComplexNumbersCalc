from random import randint
class randomColor:
    def __init__(self):
        self.r = randint(0, 255) / 255
        self.g = randint(0, 255) / 255
        self.b = randint(0, 255) / 255
        self.rColor = (self.r, self.g, self.b)
