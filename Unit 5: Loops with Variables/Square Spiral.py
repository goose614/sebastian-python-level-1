import turtle
import random
size = 70
t = turtle.Turtle()
t.speed(200)
r = random.randint(0,255)
g = random.randint(0,255)
b = random.randint(0,255)
t.color(r,g,b)
for i in range(100):
  t.forward(size)
  t.right(90)
  
  size = size + 10
  
  
