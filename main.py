# Etch A Sketch example using turtle graphices
# Demonstrates turtle graphics and event listners in python
# 18/06/2023

from turtle import Turtle, Screen
tim = Turtle()
screen = Screen()


def move_forwards():
    tim.forward(10)


screen.listen()
screen.onkey(key="space", fun=move_forwards)


screen.exitonclick()
