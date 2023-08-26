import math

import matplotlib.pyplot as plt
from matplotlib import patches

from complexNum import ComplexNumClass as complexN
from polarNum import PolarNumClass as polarN

from randomColorFunc import randomColor


fig, ax = plt.subplots()


def create_graph(a):
    a = a + 0.5
    ax.axhline(0, color='black'), ax.axvline(0, color='black')
    ax.set_xlim(-a, a), ax.set_ylim(-a, a)
    ax.set_aspect(1)
    return ax


def create_circle(b):
    ax = create_graph(b)
    drawing_circle = plt.Circle((0, 0), b, fill=False)
    ax.add_artist(drawing_circle)


def draw_angle(angle_a, angle_b, radius, color):
    if (angle_a % 360) < (angle_b % 360):
        angle_b, angle_a = angle_a, angle_b

    angle_a_copy = angle_a
    angle_b_copy = angle_b

    sign_radius = radius * 0.2
    middle_angle = (angle_a + angle_b) / 2
    angle_deg = abs(angle_a - angle_b)

    if angle_a - angle_b > 180:
        angle_a_copy, angle_b_copy = angle_b, angle_a
        middle_angle = (angle_a + angle_b) / 2 + 180
        angle_deg = 360 - abs(angle_a - angle_b)

    arc = patches.Arc((0, 0), 2 * sign_radius, 2 * sign_radius, angle=0, theta1=angle_b_copy, theta2=angle_a_copy,
                      color=color, linewidth=1.5)

    radius_angle_text = 1.35 * sign_radius
    text_x = radius_angle_text * math.cos(math.radians(middle_angle))
    text_y = radius_angle_text * math.sin(math.radians(middle_angle))
    plt.text(text_x, text_y, f"{angle_deg:.2f}°", color=color, ha='center', va='center')

    ax.add_patch(arc)


def enter_point():
    while True:
        print("Complex or polar?")
        x = input().lower()
        if x == "complex":
            try:
                real = float(input("Real: "))
                image = float(input("Image: "))
                return complexN(real, image)
            except ValueError:
                print("Invalid input, please enter valid numbers for the real and image parts.")

        elif x == "polar":
            try:
                radius = float(input("Radius: "))
                angle = float(input("Angle: "))
                return polarN(radius, angle)
            except ValueError:
                print("Invalid input, please enter valid numbers for the radius and angle parts.")

        else:
            print("Invalid input. Please enter 'complex' or 'polar'.")


def run():
    z = enter_point()
    zColor = randomColor()
    create_circle((z.radius))
    plt.scatter(z.real, z.image, color="red")
    plt.plot([0, z.real], [0, z.image], color=zColor.rColor)
    draw_angle(z.angle, 0, z.radius, zColor.rColor)
    print(z.angle)
    print(zColor.rColor)
    plt.show()

def mainRun():
    while True:
        run()
        print("another number?")
        x = input().lower()
        if x == "yes":

