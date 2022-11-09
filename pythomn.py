from turtle import Turtle,Screen
turtle=Turtle()
screen = Screen()
from turtle import*
bgcolor("black")
speed(0)
hideturtle()
for i in range(177):
    turtle.pencolor("orange")
    turtle.circle(i*1)
    right(4)
    forward(4)
    speed(0)

exitonclick()