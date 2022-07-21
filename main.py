import turtle
from turtle import Turtle, colormode
import random

colormode(255)

color_list = [(227, 227, 220), (219, 224, 218), (184, 55, 31), (209, 157, 79), (142, 35, 46), (167, 54, 77),
              (43, 97, 159),
              (97, 169, 201), (212, 165, 17), (196, 84, 131), (77, 162, 111), (89, 186, 131), (60, 129, 37),
              (37, 60, 122),
              (213, 118, 150), (233, 190, 117), (76, 51, 39), (41, 150, 203), (229, 67, 30), (241, 220, 225),
              (91, 104, 17),
              (217, 231, 239), (57, 52, 71), (65, 43, 53), (179, 27, 23), (238, 197, 6), (227, 170, 181),
              (174, 204, 183),
              (234, 172, 163), (163, 203, 213)]

a = Turtle()

random_color = random.choice(color_list)
start_x=-300
start_y=-300
a.speed("fastest")

for time in range(0,10):
 a.penup()
 a.setx(start_x)
 a.sety(start_y + time*50)
 a.dot(20, random.choice(color_list))
 # print(a.position())
 for n in range(1, 10):
     a.penup()
     a.forward(50)
     a.dot(20, random.choice(color_list))
     a.hideturtle()











screen = turtle.Screen()

screen.exitonclick()
