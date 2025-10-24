import turtle
t = turtle.Turtle()
t.speed(29333)
r = 40
g = 30
b = 40
for i in range(72):
  size = 30
  t.color(r,g,b)
  for j in range(3):
    for s in range(4):
      t.forward(size) 
      t.right(90)
   
  
    size = size + 25
  t.left(5)
  r = r +5
