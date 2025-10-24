import turtle
t = turtle.Turtle()
t.color("pink")
screen = turtle.Screen()
def drawrectangle(x,y):
  for i in range(2):
    t.begin_fill()
    t.forward(x)
    t.right(90)
    t.forward(-y)
    t.right(90)
    t.end_fill()
screen.onclick(drawrectangle)
    
drawrectangle(190,90)