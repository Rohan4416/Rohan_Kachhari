import turtle

# Create a turtle object
t = turtle.Turtle()

# Move the turtle to the starting position of the rectangle
t.penup()
t.goto(-100, 100)
t.pendown()

# Draw the rectangle orange color
t.color("orange")
t.begin_fill()
for i in range(2):
    t.forward(300)
    t.right(90)
    t.forward(100)
    t.right(90)
t.end_fill()
#Position to draw green
t.penup()
t.goto(-100,-100)
t.pendown()
#draw the green rectangle
t.color("green")
t.begin_fill()
for i in range(2):
    t.forward(300)
    t.right(90)
    t.forward(100)
    t.right(90)
t.end_fill()
#positon to draw ashok chakra
t.penup()
t.goto(50,-50)
t.pendown()
#make ashok chakra
turtle.bgcolor("white")
t.pencolor("blue")
for i in range(24):
    t.forward(50)
    t.backward(50)
    t.left(15)

t.penup()
t.goto(50,-100)
t.pendown()
t.circle(50)
# Keep the window open
turtle.done()

