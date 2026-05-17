import turtle
import math

s = turtle.Screen()
s.bgcolor("#c8b89a")
s.title("Long Nose Dog - Close Up")
s.setup(600, 700)

t = turtle.Turtle()
t.speed(0)
t.hideturtle()

def goto_fill(points, fill, border="#5a3e28", bsize=2):
    t.penup()
    t.goto(points[0])
    t.pendown()
    t.fillcolor(fill)
    t.pencolor(border)
    t.pensize(bsize)
    t.begin_fill()
    for p in points[1:]:
        t.goto(p)
    t.goto(points[0])
    t.end_fill()

def oval(x, y, rx, ry, fill, border="#5a3e28", bsize=2):
    t.penup()
    t.goto(x + rx, y)
    t.pendown()
    t.fillcolor(fill)
    t.pencolor(border)
    t.pensize(bsize)
    t.begin_fill()
    for i in range(360):
        angle = math.radians(i)
        px = x + rx * math.cos(angle)
        py = y + ry * math.sin(angle)
        t.goto(px, py)
    t.end_fill()

# Background fur / head shape (white/cream dog)
oval(0, 80, 280, 200, "#f0ece0", "#d4c9b0", 1)

# Long snout - main body coming toward viewer (foreshortened)
# Snout is wide at top, narrows slightly, then big bulbous nose tip
goto_fill([
    (-130, 60), (130, 60),
    (155, 0), (160, -80),
    (140, -180), (100, -280),
    (60, -330), (0, -350),
    (-60, -330), (-100, -280),
    (-140, -180), (-160, -80),
    (-155, 0)
], "#e8e0d0", "#b0a090", 1)

# Snout center ridge
t.penup()
t.goto(0, 50)
t.pendown()
t.pencolor("#d0c8b8")
t.pensize(1)
t.goto(0, -280)

# Fur texture lines on snout
for xi in [-80, -50, -20, 20, 50, 80]:
    t.penup()
    t.goto(xi, 30)
    t.pendown()
    t.pencolor("#d8d0c0")
    t.pensize(1)
    t.goto(xi * 1.1, -100)

# Nose tip - dark grey/black bulbous end
oval(0, -300, 90, 65, "#3a3530", "#1a1510", 2)
oval(-20, -290, 35, 28, "#4a4540", "#3a3530", 1)
oval(25, -295, 30, 25, "#4a4540", "#3a3530", 1)

# Nostril holes
oval(-28, -305, 22, 16, "#1a1008", "#1a1008", 1)
oval(28, -305, 22, 16, "#1a1008", "#1a1008", 1)

# Nose shine
oval(-15, -285, 12, 7, "#5a5550", "#5a5550", 0)
oval(20, -288, 8, 5, "#5a5550", "#5a5550", 0)

# Whiskers - long and droopy like the photo
whiskers = [
    # left side whiskers
    [(-120, -180), (-280, -220)],
    [(-115, -200), (-290, -260)],
    [(-118, -220), (-285, -300)],
    [(-110, -160), (-275, -180)],
    # right side whiskers
    [(120, -180), (280, -220)],
    [(115, -200), (290, -260)],
    [(118, -220), (285, -300)],
    [(110, -160), (275, -180)],
]
for w in whiskers:
    t.penup()
    t.goto(w[0])
    t.pendown()
    t.pencolor("#c8c0b0")
    t.pensize(1)
    t.goto(w[1])

# Eyes at top - looking down at us
# Left eye
oval(-160, 160, 55, 48, "white", "#2a1a0a", 2)
oval(-162, 155, 36, 34, "#1a0800", "#1a0800", 1)
oval(-158, 158, 22, 21, "#0a0400", "#0a0400", 1)
oval(-150, 163, 9, 8, "white", "white", 0)
oval(-168, 160, 5, 5, "white", "white", 0)

# Right eye
oval(160, 160, 55, 48, "white", "#2a1a0a", 2)
oval(162, 155, 36, 34, "#1a0800", "#1a0800", 1)
oval(158, 158, 22, 21, "#0a0400", "#0a0400", 1)
oval(150, 163, 9, 8, "white", "white", 0)
oval(168, 160, 5, 5, "white", "white", 0)

# Eyebrow fur tufts
t.penup()
t.goto(-210, 195)
t.pendown()
t.pencolor("#b0a890")
t.pensize(2)
t.goto(-130, 205)
t.penup()
t.goto(130, 205)
t.pendown()
t.goto(210, 195)

# Floor/ground at bottom
goto_fill([
    (-300, -380), (300, -380),
    (300, -350), (-300, -350)
], "#8b7355", "#8b7355", 0)

turtle.done()
