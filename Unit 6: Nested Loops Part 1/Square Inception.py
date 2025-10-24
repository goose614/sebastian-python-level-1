import turtle
t = turtle.Turtle()
t.speed(29333)
for i in range(4):
  size = 30
  for j in range(3):
    for s in range(4):
      t.forward(size) 
      t.right(90)
   
  
    size = size + 25
  t.left(5)