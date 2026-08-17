from turtle import *
from random import random, choice

tim = Turtle()
tim.speed(0)
tim.pensize(2)

x = 100
colours = ["CornflowerBlue","DarkOrchid","IndianRed","DeepSkyBlue",
           "LightSeaGreen","Wheat","SlateGray","SeaGreen"]
for i in range(50):
    tim.color(choice(colours))
    tim.circle(x)
    tim.setheading(tim.heading() + 10)

screen = Screen()
screen.exitonclick()