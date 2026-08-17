from turtle import *
from random import random, choice

tim = Turtle()
tim.pensize(15)
colours = ["CornflowerBlue","DarkOrchid","IndianRed","DeepSkyBlue",
           "LightSeaGreen","Wheat","SlateGray","SeaGreen"]
directions = [0, 90, 180, 270]

for i in range(100):
    tim.color(choice(colours))
    tim.forward(30)
    tim.setheading(choice(directions))

screen = Screen()
screen.exitonclick()