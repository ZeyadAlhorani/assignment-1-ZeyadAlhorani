
import turtle


def draw_rectangle():

    XMAX =200
    XMIN =-XMAX
    YMAX =200
    YMIN =-YMAX


shapeinput: str = input("choose either r for rectangle, c for circle, t for tringle")
colorinput = input("red , navy , or green")
length: float = input("put a length")
width: float = input("put a width")

if shapeinput == "r":
    draw_rectangle()

else: shapeinput: == "c":
    radius: float = input("put a radius")
    draw_circle()

elif: shapeinput == "t":
    draw_triangle()


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

def draw_rectangle():
    turtle.penup()
    turtle.goto(180,50)
    turtle.pendown()
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

def draw_circle():
    turtle.penup()
    turtle.goto(-130,10)
    turtle.pendown()
    turtle.begin_fill()
    turtle.circle(60)
    turtle.fillcolor("navy")
    turtle.end_fill()

def draw_triangle():
    turtle.penup()
    turtle.goto(-150,100)
    turtle.pendown()
    turtle.begin_fill()
    turtle.forward(100)
    turtle.left(120)
    turtle.forward(100)
    turtle.left(120)
    turtle.forward(100)
    turtle.fillcolor("green")
    turtle.end_fill()

draw_triangle()
draw_circle()
draw_triangle()
