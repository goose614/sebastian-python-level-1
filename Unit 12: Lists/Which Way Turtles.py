import turtle
import random
t = turtle.Turtle()
turtles = []
for i in range(100):
  t = turtle.Turtle()
  turtles.append(t)
  t.goto(0,0)
  x = random.randint(15,360)
  t.right(x)
  t.forward(200)