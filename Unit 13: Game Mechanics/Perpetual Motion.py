import turtle
t = turtle.Turtle()
screen = turtle.Screen()  
  
def right():
  t.right(3)

def left():
  t.left(3)

screen.onkey(left,"left")
screen.onkey(right,"right") 
  
  
screen.listen()


while True:
  t.forward(1)