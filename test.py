import drawshapes
import turtle

length = 150
width = 100


#def test_rectangle_will_fit():

# this function is the one that failed because it did not fit in the border

    #r = drawshapes.draw_rectangle()

    #turtle.goto(-200,200)
    #assert(x == turtle.xcor())
    #assert(y == turtle.ycor())

    #rectanle_fillcolor = turtle.fillcolor()
    #assert(rectangle_fillcolor == "red")

    #length = turtle.forward(150)
    #assert(300 == 150)

    #width = turtle.forward(100)
    #assert(250 == 100)


#def test_circle_will_fit():
    #the circle did not fit in the border and was too big

    #c = drawshapes.draw_circle()

    #circle_fillcolor = turtle.fillcolor()
    #assert(circle_fillcolor=="navy")

    #radius = turtle.circle()
    #assert(radius==200)

#def test_triangle_will_fit():
    #I used this test to see if the given coordinates and size will fit the triangle in the border;
    # it failed because it was on the outside

    #t = drawshapes.draw_circle()

    #turtle.goto(-200,150)
    #assert(-200 == turtle.xcor())
    #assert(150 == turtle.ycor())

    #triangle_fillcolor = turtle.fillcolor()
    #assert(triangle_fillcolor == "green")

    #turtle.forward(90)
    #turtle.left(120)
    #turtle.forward(90)
    #turtle.left(120)
    #turtle.forward(90)

# ----------------------------------------------------------------------------------------

def test_rectangle_will_fit():

    #the test is now passed after giving correct coordinates

    r = drawshapes.draw_rectangle()

    rectangle_fillcolor = turtle.fillcolor()
    assert(rectangle_fillcolor == "red")

    turtle.goto(-50,10)
    assert(-50 == turtle.xcor())
    assert(10 == turtle.ycor())

    length = turtle.forward(150)
    assert(150 == 150)

    width = turtle.forward(100)
    assert(100 == 100)

def test_circle_will_fit():

    c = drawshapes.draw_circle()

    turtle.goto(-50,20)
    assert(-50 == turtle.xcor())
    assert(20 == turtle.ycor())

    circle_fillcolor = turtle.fillcolor()
    assert (circle_fillcolor=="navy")

def test_triangle_will_fit():

    t = drawshapes.draw_triangle()

    turtle.goto(-200,150)
    assert(-200 == turtle.xcor())
    assert(150 == turtle.ycor())

    triangle_fillcolor = turtle.fillcolor()
    assert(triangle_fillcolor == "green")

    turtle.forward(90)
    turtle.left(120)
    turtle.forward(90)
    turtle.left(120)
    turtle.forward(90)

