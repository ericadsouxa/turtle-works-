import turtle
import random  #import random module

turtle.bgcolor('black')
turtle.left(90)
turtle.speed(0)
turtle.color('green')
turtle.pensize(4) #change pensize as per requirement 



def draw_fractal(blen):
    sfcolor =["white","blue", "purple","yellow", "green"] #optional to add shades of green for reel tree effect
    turtle.color(random.choice(sfcolor))


    if(blen<10):
        return

    else:
        turtle.forward(blen)
        turtle.left(30)
        draw_fractal(3*blen/4)
        turtle.right(60)
        draw_fractal(3 * blen / 4)
        turtle.left(30)
        turtle.backward(blen)


draw_fractal(90)  ##placing tree graphic in centre
turtle.done()
