import turtle
import random
t = turtle.Turtle()
t.penup()
x = random.randint(-150,150)
y = random.randint(-150,150)
t.goto(x,y)
t.pendown()
if x > 0 and y > 0:
  t.color("blue")
  for i in range(4):
    t.forward(80)
    t.right(90)
if x < 0 and y > 0:
  t.color("orange")
  for i in range(4):
    t.forward(80)
    t.right(90)
if x < 0 and y < 0:
  t.color("green")
  for  i in range(4):
    t.forward(80)
    t.right(90)
if x > 0 and y < 0:
  t.color("yellow")
  for i in range(180):
    t.forward(2)
    t.right(2)
  