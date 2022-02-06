#turtle works is amzing graphics 
#spiral circle 
#hypnotic effect 
#black background 
#-------------------------------------------------------------------------------------
#-------------------------------------------------------------------------------------

import turtle
t = turtle.Turtle()
turtle.bgcolor("black")
turtle.speed(100)
t.color("white")
t.pensize(4)

r = 10


for i in range(100):
    t.circle(r +i, 45)
