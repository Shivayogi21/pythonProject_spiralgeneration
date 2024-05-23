from turtle import Screen
import random
import turtle

t = turtle.Turtle()
turtle.colormode(255)

turtle.speed('fastest')


def random_color():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    color = (r, g, b)
    return color


def draw_sprial(size_of_gap):
    for i in range(int(360/size_of_gap)):
        t.color(random_color())
        t.circle(100)
        t.setheading(t.heading() + size_of_gap)


draw_sprial(5)



screen = turtle.Screen()
screen.exitonclick()

