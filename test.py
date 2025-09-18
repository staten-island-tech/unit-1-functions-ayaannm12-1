import turtle
from turtle import *
t = Turtle()

t.speed(0)

t.shape('turtle')
def star(length,deg):
    for i in range(5):
        t.forward(length)
        t.right(deg)
# square(100,90)

    


def addStars(iRange):
    length = 25
    for i in range(iRange):
        star(length, 144)
        length += 10
        t.right(5)
addStars(60)
turtle.done()