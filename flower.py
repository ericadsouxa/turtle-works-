import turtle
t=turtle.Turtle()
s=turtle.Screen()
s.bgcolor("black")
t.pencolor("yellow")
t.speed(20)
for i in range(150):
    t.circle(190-i,98)
    t.lt(90)
    t.circle(190-i,98)
    t.lt(18)

turtle.exitonclick()