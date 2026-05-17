import turtle

s = turtle.Screen()
s.bgcolor("white")
s.title("Long Nose Dog")
s.setup(500, 700)

t = turtle.Turtle()
t.speed(0)
t.hideturtle()
t.pensize(3)
t.pencolor("black")

# Long body / snout - big oval teardrop shape
t.fillcolor("white")
t.penup()
t.goto(0, 280)
t.pendown()
t.begin_fill()
t.goto(120, 240)
t.goto(150, 160)
t.goto(155, 60)
t.goto(150, -60)
t.goto(130, -160)
t.goto(100, -240)
t.goto(60, -300)
t.goto(0, -330)
t.goto(-60, -300)
t.goto(-100, -240)
t.goto(-130, -160)
t.goto(-150, -60)
t.goto(-155, 60)
t.goto(-150, 160)
t.goto(-120, 240)
t.goto(0, 280)
t.end_fill()

# Left eye white
t.fillcolor("white")
t.penup()
t.goto(-115, 180)
t.pendown()
t.begin_fill()
t.circle(45)
t.end_fill()

# Right eye white
t.penup()
t.goto(70, 180)
t.pendown()
t.begin_fill()
t.circle(45)
t.end_fill()

# Left pupil
t.fillcolor("black")
t.penup()
t.goto(-100, 188)
t.pendown()
t.begin_fill()
t.circle(28)
t.end_fill()

# Right pupil
t.penup()
t.goto(85, 188)
t.pendown()
t.begin_fill()
t.circle(28)
t.end_fill()

# Left eye shine
t.fillcolor("white")
t.penup()
t.goto(-92, 208)
t.pendown()
t.begin_fill()
t.circle(10)
t.end_fill()

# Right eye shine
t.penup()
t.goto(93, 208)
t.pendown()
t.begin_fill()
t.circle(10)
t.end_fill()

# Nose - small black oval at bottom
t.fillcolor("black")
t.penup()
t.goto(-25, -320)
t.pendown()
t.begin_fill()
t.circle(25)
t.end_fill()

# Small ear lines at top
t.penup()
t.goto(-80, 265)
t.pendown()
t.pensize(2)
t.goto(-60, 290)
t.goto(-30, 275)

t.penup()
t.goto(80, 265)
t.pendown()
t.goto(60, 290)
t.goto(30, 275)

turtle.done()