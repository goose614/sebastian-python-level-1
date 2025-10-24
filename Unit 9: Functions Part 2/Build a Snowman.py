import turtle
t = turtle.Turtle()
def drawcircle(size):
  for i in range(120):
    t.forward(size)
    t.right(3)
    
drawcircle(8)
t.right(180)
drawcircle(5)
t.right(90)
t.penup()
t.forward(191)
t.right(260)
t.pendown()
drawcircle(3)