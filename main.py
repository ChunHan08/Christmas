from turtle import *
from Figures import *
from random import randint 
speed(0)

bg = turtle.Screen()
bg.bgcolor("#007CFF")

y = -100
width = 240

box1(turtle, "#461F00", -15, y - 40, 30, 40)

while width > 20 :
  width = width - 20
  height = randint(20,30)
  x = 0 - width/2
  box1(turtle, "#006A16", x, y, width, height)
  balls(turtle, "#FF770C", x, y, 5)
  balls(turtle, "#FF0000", 2, y, 5)
  balls(turtle, "#FF770C", -x, y, 5)
  y = y + height
  
star(turtle, "#e6e600", 0.7, y, 20)

penup()
color("#C9E7FF")
goto(-250, -250)
write("Merry Christmas !!!", font=("Calibri", 40, "bold"))


hideturtle()

turtle.done()