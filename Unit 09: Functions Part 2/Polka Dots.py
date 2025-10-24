import turtle
import random
t = turtle.Turtle()
t.speed(200)
screen = turtle.Screen()
t.color("black")
def drawcircle(x,y):
  t.penup()
  t.goto(x,y)
  t.pendown()
  size = random.randint(1,3)
  t.begin_fill()
  for i in range(120):
    t.forward(size)
    t.right(3)
  t.end_fill()
drawcircle(2,9)
screen.onclick(drawcircle)