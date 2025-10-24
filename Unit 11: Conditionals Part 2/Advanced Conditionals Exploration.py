import turtle
import random
t = turtle.Turtle()
num = random.randint(0,3)
if num == 0 :
  for i in range(4):
    t.forward(200)
    t.right(90)
elif num == 1 :
  for i in range(3):
    t.forward(100)
    t.right(120)
else :
  for i in range(180):
    t.forward(2)
    t.right(2)