"""
Based on "100 days of code" Day 19 lecture, which is to create an Etch a Sketch then a turtle race!
"""

from turtle import Turtle, Screen
from random import randint

screen = Screen()

screen.setup(width=500,height=400)

bob = Turtle(shape="turtle")
bob.penup()
bob.goto(x=-230,y=-100)

doug = Turtle(shape="turtle")
doug.color("red")
doug.penup()
doug.goto(x=-230,y=0)

def start_race():
    while True:
        bob.speed(speed=3)
        doug.speed(speed=5)
        bob.goto(x=100,y=-100)
        doug.goto(x=100,y=0)


screen.listen()
screen.onkeypress(key="g", fun=start_race)
screen.exitonclick()
