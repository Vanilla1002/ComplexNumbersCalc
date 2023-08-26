import math
from Nums import Number


class PolarNumClass(Number):
    def __init__(self, radius, angle):
        super().__init__(None, None, radius, angle)
        self.real = self.radius*math.cos(math.radians(self.angle))
        self.image = self.radius*math.sin(math.radians(self.angle))
        self.complexnum = (self.real, self.image)