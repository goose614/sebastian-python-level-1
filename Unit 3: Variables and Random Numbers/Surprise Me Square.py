import turtle 
import random

t = turtle.Turtle()
x = random.randint(-150,150)
y = random.randint(-150,150)
t.penup()
t.goto(x,y)
t.pendown()
sidelength = random.randint(10,200)
t.begin_fill()
r = random.randint(0,255)
g = random.randint(0,255)
b = random.randint(0,255)
w = random.randint(0,255)
t.color(r,g,b,)
for i in range(4):
  t.forward(sidelength)
  t.right(90)
t.end_fill()
