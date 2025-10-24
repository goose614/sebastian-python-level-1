import turtle
t = turtle.Turtle()
b = turtle.Turtle()
screen = turtle.Screen() 
b.penup()
b.goto(-300,250)
b.pendown()
for i in range(4):
  b.forward(500)
  b.right(90)


def right():
  t.right(3)

def left():
  t.left(3)

screen.onkey(left,"left")
screen.onkey(right,"right") 
  
  
screen.listen()


while True:
  t.forward(1)
  
  
  
  
  if t.xcor() >= 200:
    t.write("out of bounds!")
    break
  if t.xcor() <= -300:
    t.write("out of bounds!")
    break
  if t.ycor() <= -250:
    t.write("out of bounds!")
    break
  if t.ycor() >= 250:
    t.write("out of bounds!")
    break
















