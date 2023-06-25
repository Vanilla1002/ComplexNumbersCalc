import math


class ComplexNum:
    def __init__(self, real, imag):
        self.real = real
        self.imag = imag

    def get_the_absolute_value(self):
        radius = (self.real ** 2 + self.imag ** 2)**0.5
        return radius

    def get_angle(self):
        θ = math.degrees(math.atan2(self.imag, self.real))
        θ = round(θ, 4)
        return θ

    def complex_to_polar(self):
        r = self.the_absolute_value()
        θ = self.angle()
        w = r, θ
        return w

    def get_quadrant(self):
        if self.real > 0 and self.imag > 0:
            return 1
        if self.real < 0 and self.imag > 0:
            return 2
        if self.real < 0 and self.imag < 0:
            return 3
        if self.real > 0 and self.imag < 0:
            return 4
        if self.get_angle() == 0 or self.get_angle() == 180:
            return "point on x-axis"
        if self.get_angle() == 270 or self.get_angle() == 90:
            return "point on y-axis"



