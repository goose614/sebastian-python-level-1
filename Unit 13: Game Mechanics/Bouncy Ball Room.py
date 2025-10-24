import turtle
import random
turtles = []
for i in range(10):
  t = turtle.Turtle()
  t.speed(400000)
  
  turtles.append(t)
  t.penup()
  t.shape("circle")
  t.color("red")
  t.right(random.randint(1,360))

b = turtle.Turtle()
screen = turtle.Screen() 
b.penup()
b.goto(-300,250)
b.pendown()
for i in range(4):
  b.forward(500)
  b.right(90)
  
while True:
  for t in turtles:
    t.forward(10)
    if t.xcor() >= 200:
      t.right(90)
    if t.xcor() <= -300:
      t.right(90)
    if t.ycor() <= -255:
      t.right(90)          
    if t.ycor() >= 250:
      t.right(90)
