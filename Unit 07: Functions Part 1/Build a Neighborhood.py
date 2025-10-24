import turtle
import random
t = turtle.Turtle()
t.speed(5)
def drawSquare():
  for i in range(4):
   t.forward(35)
   t.right(90)

def drawTriangle():
  for j in range(3):
    t.left(120)
    t.forward(40)
    
def drawHouse():
  drawSquare()
  t.forward(35)
  drawTriangle()
  

  
for i in range(5):
  t.penup()
  x = random.randint(-250,250)
  y = random.randint(-250,250)
  t.goto(x,y)
  t.pendown()
  drawHouse()

  