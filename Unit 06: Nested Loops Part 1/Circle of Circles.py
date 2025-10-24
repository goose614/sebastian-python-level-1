import turtle
t = turtle.Turtle()
t.speed(0)
for i in range(90):
  t.right(10)
  for i in range(360):
    t.forward(2)
    t.right(1)
    