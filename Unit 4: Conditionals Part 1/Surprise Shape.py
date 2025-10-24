import turtle
import random
t=turtle.Turtle()
x = random.randint(1,3)
if x == 2:
  t.penup()
  t.goto(-147,27)
  t.pendown()
  for i in range(8):
    t.forward(270)
    t.right(135)
if x == 3:
  for i in range(180):
    t.forward(2)
    t.right(2)
if x == 1:
  for i in range(8):
    t.forward(70)
    t.right(45)
    
    
    
    