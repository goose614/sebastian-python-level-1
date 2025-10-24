import turtle
t = turtle.Turtle()
t.speed(4000000000000000000000)
s = 20
t.setheading(600)
t.penup()
t.goto(0,100)
t.pendown()
for i in range(50):
  for i in range(3):
   t.forward(s)
   t.left(120)
  s = s + 5