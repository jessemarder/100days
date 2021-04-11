"""
Based on "100 days of code" Day 19 lecture, which is to create an Etch a Sketch
"""

from turtle import Turtle, Screen

tim = Turtle()
screen = Screen()

def move_forward():
    tim.forward(10)

screen.listen()
screen.onkey(key="space", fun=move_forward)
screen.exitonclick()
