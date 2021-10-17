# Draws a Pythagoras tree, which is another fractal tree, using a recursive algorithm.
import turtle
import math

screen = turtle.Screen()
screen.bgcolor("skyblue")

py = turtle.Turtle()
py.shape("turtle")
py.color("darkgreen")
py.fillcolor("black")
py.speed(0)

# Draw a single square of the given size, and fill it in
def drawSquare(t, size):
    t.begin_fill()
    for i in range(4):
        t.forward(size)
        t.left(90)
    t.end_fill()
 
# Draw a node at the given level, recursively drawing all the smaller nodes
def drawNode(t, size, level):
    if (level < 1):
        return
    else:
        drawSquare(t, size)
        
        # Draw the left branch
        leftSize = size * math.sqrt(3) / 2
        t.forward(size)
        t.left(90)
        t.forward(size)
        t.right(150)
        t.forward(leftSize)
        t.left(90)
        drawNode(t, leftSize, level - 1)
        
        # Draw the right branch
        rightSize = size // 2
        t.right(180)
        t.forward(rightSize)
        t.left(90)
        drawNode(t, rightSize, level - 1)
        t.left(60)
        t.back(size)
  
# Position the turtle to start drawing!
py.penup()
py.goto(90, -150)
py.left(90)
py.pendown()

# This will take a very long time to draw!
drawNode(py, 58, 8)
py.hideturtle()