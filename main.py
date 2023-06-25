import math
import matplotlib.pyplot as plt
import complexNum


def  the_absolute_value(x,y):
    return math.sqrt(x**2+y**2)


def complex_to_polar(x, y):
    z = complex(x, y)
    r = the_absolute_value(z.real, z.imag)
    θ = math.degrees(math.atan2(y, x))
    w = r, θ
    return w

def printW(x):
    a = x[0]
    b = x[1]
    print(f'{a:.2f} * cis({b:.2f})')







# Creates the graph
fig, ax = plt.subplots()
ax.axhline(0, color='black'), ax.axvline(0, color='black')
ax.set_xlim(-1.2, 1.2), ax.set_ylim(-1.2, 1.2)
ax.set_aspect(1)
Drawing_circle = plt.Circle((0, 0), 1, fill=False)
ax.add_artist(Drawing_circle)
plt.show()
