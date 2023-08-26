import math
from Nums import Number


class ComplexNumClass(Number):
    def __init__(self, real, image):
        self.radius = (real ** 2 + image ** 2) ** 0.5
        self.angle = round((math.degrees(math.atan2(image, real))), 4)
        self.polarNum = (self.radius, self.angle)
        super().__init__(real, image, self.radius, self.angle)
