
import turtle

def draw_rectangle():

    XMAX =200
    XMIN =-XMAX
    YMAX =200
    YMIN =-YMAX

length = 150
width = 100

turtle.penup()
turtle.goto(-200,-200)
turtle.pendown()
turtle.goto(200,-200)
turtle.goto(200,200)
turtle.goto(-200,200)
turtle.goto(-200,-200)
turtle.penup()
turtle.goto(0,0)
turtle.pendown()
turtle.begin_fill()
turtle.fillcolor()

def rectangle_will_fit():
    turtle.begin_fill()
    turtle.forward(length)
    turtle.right(90)
    turtle.forward(width)
    turtle.right(90)
    turtle.forward(length)
    turtle.right(90)
    turtle.forward(width)
    turtle.right(90)
    turtle.fillcolor("red")
    turtle.end_fill()

rectangle_will_fit()



