class Number:
    def __init__(self, real, image, radius, angle):
        self.real = real
        self.image = image
        self.radius = abs(radius)
        self.angle = angle
        if -360 <= angle < 0:
            self.angle += 360
        elif -360 > angle:
            x = abs(self.angle)
            x = 360 - (x % 360)
            self.angle = x
        if angle >= 360:
            self.angle = angle % 360

    def get_quadrant(self):
        if self.real > 0 and self.image > 0:
            return 'I'
        if self.real < 0 < self.image:
            return 'II'
        if self.real < 0 and self.image < 0:
            return 'II I'
        if self.real > 0 > self.image:
            return 'IV'
        if self.angle == 0 or self.angle == 180:
            return "point on x-axis"
        if self.angle == 270 or self.angle == 90:
            return "point on y-axis"

    def printW(self):
        print(f'{self.radius:.2f} * cis({self.angle:.2f})')

    def printZ(self):
        print((self.real, self.image))