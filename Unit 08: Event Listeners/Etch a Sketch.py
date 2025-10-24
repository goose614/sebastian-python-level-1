import turtle
t = turtle.Turtle()
t.speed(10000)
screen = turtle.Screen()
t.goto(0,0)

def right():
  t.right(1)

def left():
  t.left(1)


def up():
  t.setheading
  t.forward(10)

def down():
  t.setheading
  t.forward(-10)
  
screen.onkey(left,"left")
screen.onkey(right,"right")  
screen.onkey(up,"up")
screen.onkey(down,"down")

screen.listen()