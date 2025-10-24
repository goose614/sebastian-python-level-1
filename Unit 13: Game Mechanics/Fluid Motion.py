import turtle
t = turtle.Turtle()
t.speed(200)
screen = turtle.Screen() 
screen.tracer(0)
for i in range(200):
  t.forward(2)
  t.clear()
  for i in range(60):
    t.forward(6)
    t.right(6)
  screen.update() 