import math
import matplotlib.pyplot as plt


def  theAbsoluteValue(x,y):
    return math.sqrt(x**2+y**2)



def  complexToPolar(x, y):
    z = complex(x, y)
    r = theAbsoluteValue(z.real, z.imag)
    θ = math.degrees(math.atan2(y, x))
    w = r, θ
    return w

def printW(x):
    a = x[0]
    b = x[1]
    print(f'{a:.2f} * cis({b:.2f})')

printW (complexToPolar(5,4))








# Creates the graph
fig, ax = plt.subplots()
ax.axhline(0, color='black'), ax.axvline(0, color='black')
ax.set_xlim(-1.2, 1.2), ax.set_ylim(-1.2, 1.2)
ax.set_aspect(1)
Drawing_circle = plt.Circle((0, 0), 1, fill=False)
ax.add_artist(Drawing_circle)
plt.show()
