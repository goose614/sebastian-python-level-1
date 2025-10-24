import turtle
t = turtle.Turtle()
def drawsquare(size):
   for i in range(4):
     t.forward(size)
     t.right(90)
drawsquare(60)
def drawtriangle(size):
  for i in range(3):
    t.forward(size)
    t.right(120)
drawtriangle(200)