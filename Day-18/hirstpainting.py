from turtle import *
from random import random, choice

# import colorgram
#
#
# rgb_colors=[]
# colors = colorgram.extract('image.jpg',30)
# for color in colors:
#     r=color.rgb.r
#     g=color.rgb.g
#     b=color.rgb.b
#     new_color = (r,g,b)
#     rgb_colors.append(new_color)
# print(rgb_colors)
screen = Screen()
color_list=[(235, 229, 232), (236, 35, 109), (220, 230, 237), (142, 27, 67), (228, 238, 232), (240, 74, 36), (8, 147, 94), (219, 169, 47), (182, 159, 48), (45, 191, 232), (29, 127, 194), (247, 219, 38), (125, 192, 82), (253, 223, 0), (181, 39, 99), (83, 24, 88), (37, 172, 115), (210, 132, 166), (212, 57, 30), (235, 164, 194), (154, 27, 24), (238, 169, 158), (162, 211, 179), (4, 115, 51), (25, 185, 222), (135, 211, 231), (70, 136, 188), (112, 11, 10), (165, 194, 223)]
screen.colormode(255)
tim=Turtle()
tim.hideturtle()
tim.penup()
tim.speed(0)
tim.setheading(225)
tim.forward(250)
tim.setheading(0)


dots=100

for dot_count in range(1,dots+1):
    tim.dot(20,choice(color_list))
    tim.forward(50)
    if dot_count% 10 == 0:
        tim.setheading(90)
        tim.forward(50)
        tim.setheading(180)
        tim.forward(500)
        tim.setheading(0)


screen.exitonclick()