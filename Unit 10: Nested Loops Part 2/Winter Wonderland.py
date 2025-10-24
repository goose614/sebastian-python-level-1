import turtle
t = turtle.Turtle()
t.color(9,230,193)
t.pensize(4)

def drawV ():
  t.left(45)
  t.forward(20)
  t.backward(20)
  t.right(90)
  t.forward(20)
  t.backward(20)
  t.left(45)
  t.forward(20)
def drawbranch():
  for i in range(7):
    drawV()
  t.backward(140)
for i in range(18):
  drawbranch()
  t.left(20)