import turtle
import random

t = turtle.Turtle()

for i in range(60):
  t.forward(6)
  t.right(6)
  
t.penup()



x =random.randint(-100,100)
y =random.randint(-100,100)
  
t.goto(x,y)

t.pendown()

r =random.randint(0,255)
g =random.randint(0,255)
b =random.randint(0,255)
t.color(r,g,b)
for i  in range(60):
  t.forward(6)
  t.right(6)
