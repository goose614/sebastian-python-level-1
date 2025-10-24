import turtle
import random
t = turtle.Turtle()
t.speed(10000000000000)
length = 30
for i in range(10000):
  r = random.randint(0,255)
  g = random.randint(0,255)
  b = random.randint(0,255)
  t.color(r,g,b)

  t.forward(length)
  t.backward(length)
  t.right(10)
  length = length + 1