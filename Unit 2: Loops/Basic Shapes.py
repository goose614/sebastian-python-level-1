import turtle
t= turtle.Turtle()
t.color("green")
t.begin_fill()
for i in range(200):
   t.forward(2)
   t.right(2)
t.end_fill()
t.goto(50,50)
t.color("blue")
t.begin_fill()
for i in range(4):
  t.forward(100)
  t.right(90)
t.end_fill()
t.goto(50,50)
t.color("red")
t.begin_fill()
for i in range(3):
  t.forward(45)
  t.left(120) 
t.end_fill()