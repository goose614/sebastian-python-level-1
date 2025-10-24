import turtle
import random
t = turtle.Turtle()
t.shape("turtle")
t.pensize(50)
for i in range(100):
  r = random.randint(0,255)
  g = random.randint(0,255)
  b = random.randint(0,255)
  
  t.color(r,g,b)
  x = random.randint(20,200)
  y = random.randint(20,200)
  t.goto(x,y)
  
  t.right(random.randint(10,47))

