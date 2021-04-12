"""
Based on "100 days of code" Day 19 lecture, which is to create an Etch a Sketch then a turtle race!
"""

from turtle import Turtle, Screen
from random import randint

class TurtleRace:

    def __init__(self):

        self.game_setup()
        self.winner = None

    def game_setup(self):
        """Resets the screen and asks for how many turtles to send to the races"""

        self.screen = Screen()

        self.screen.setup(width=500, height=400)

        self.screen.clearscreen()

        self.num_turtles = int(self.screen.numinput("num_turtle", "How many turtles race today?", 2, 2, 5))

        # Sets initial parameters for the turtles - 5 options
        self.names = ["Bob", "John", "Sally", "Rufus", "Marvin"]
        self.colors = ["red", "purple", "green", "yellow", "orange"]
        self.turtley = [-150, -50, 0, 50, 150]
        self.start = -230
        self.is_winner = False

        self.turtles = {}

        self.create_turtles()

        self.play()

    def create_turtles(self):
        """Generates the turtles!!"""
        for turtle_ind in range(self.num_turtles):
            self.turtles[self.names[turtle_ind]]=(Turtle(shape="turtle"))
            self.turtles[self.names[turtle_ind]].color(self.colors[turtle_ind])
            self.turtles[self.names[turtle_ind]].penup()
            self.turtles[self.names[turtle_ind]].goto(x=self.start,y=self.turtley[turtle_ind])



    def start_race(self):

        while not self.is_winner:

            for turtle in self.turtles:
                this_turtle = self.turtles[turtle]
                xchange=randint(1,10)
                next_x = this_turtle.xcor()+xchange
                this_turtle.goto(x=next_x,y=this_turtle.ycor())
                if next_x>=230:
                    self.winner = turtle
                    self.is_winner = True
                    break
                # self.is_winner(next_x)
        self.end_race()

    def end_race(self):

        print(f"We have a winner! Great job, {self.winner}!!!")
        print("Replay? Press r")

    def play(self):
        """Listens for player input"""
        self.screen.listen()
        self.screen.onkeypress(key="g", fun=self.start_race)
        self.screen.onkeypress(key="r", fun=self.game_setup)
        self.screen.exitonclick()

race=TurtleRace()