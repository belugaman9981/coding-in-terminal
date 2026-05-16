
import turtle as t

# Setup
t.speed(5)
t.pensize(3)

# Move to the center/starting point
t.penup()
t.goto(0, 50)
t.pendown()

# Draw the nose (a small filled black circle)
t.color('black')
t.begin_fill()
t.circle(15)  # Creates a nose with a 15-pixel radius
t.end_fill()

# Draw the snout/mouth line downward
t.right(90)
t.forward(30)

t.done()
