import math
class Ones_threes_nines:
    def __init__(self, number):
        self.ones = number
        self.threes = math.floor(number / 3)
        self.nines = math.floor(number / 9)