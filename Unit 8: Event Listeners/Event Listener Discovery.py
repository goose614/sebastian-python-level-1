import turtle
t = turtle.Turtle()
t.goto(0,0)
screen = turtle.Screen()
def square():
  for i in range(4):
    t.forward(60)
    t.right(90)
  
screen.onkey(square,"1")

screen.listen()
  