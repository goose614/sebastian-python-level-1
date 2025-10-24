import turtle
import random
t = turtle.Turtle()
def randomSpot():
  t.penup()
  x = random.randint(-250,250)
  y = random.randint(-250,250)
  t.goto(x,y)
  t.pendown()
  
randomSpot()
  
def randomcolor():
  r = random.randint(0,255)
  g = random.randint(0,255)
  b = random.randint(0,255)
  t.color(r,g,b)
  
randomcolor()

def reset():
  t.penup()
  t.goto(-0,0)
  t.setheading(0)
  
reset()

