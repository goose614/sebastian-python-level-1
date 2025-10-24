import turtle
import random
turtles = []
for i in range(10):
  t = turtle.Turtle()
  t.speed(400000)
  
  turtles.append(t)
  t.penup()
  t.shape("circle")
  t.color("red")
  t.right(random.randint(1,360))

b = turtle.Turtle()
screen = turtle.Screen() 
b.penup()
b.goto(-300,250)
b.pendown()
for i in range(4):
  b.forward(500)
  b.right(90)
  
s = turtle.Turtle()
s.penup()
s.goto(-300,270)
score = 0
s.write("score:" + str(score))
  
  
a = turtle.Turtle()
a.color("blue")
a.shape("turtle")
a.penup()
screen = turtle.Screen() 


def right():
  a.right(10)

def left():
  a.left(10)

screen.onkey(left,"left")
screen.onkey(right,"right") 
  
  
screen.listen()
 
while True:
  a.forward(40)
  if a.xcor() >= 200:
    a.right(90)
  if a.xcor() <= -300:
    a.right(90)
  if a.ycor() <= -250:
    a.right(90)
  if a.ycor() >= 250:
    a.right(90)
    
  for t in turtles:
    if -15 <= t.xcor() -a.xcor() <= 15 and -15 <= t.ycor() -a.ycor() <= 15:
      t.hideturtle()
      score = score + 1
      s.clear()
      s.write("score:" + str(score))
      x = random.randint(-300,200)
      y = random.randint(-255,250)
      t.goto(x,y)
      t.showturtle()
      t.right(random.randint(-300,200))

    t.forward(10)
    if t.xcor() >= 200:
      t.right(90)
    if t.xcor() <= -300:
      t.right(90)
    if t.ycor() <= -255:
      t.right(90)          
    if t.ycor() >= 250:
      t.right(90)

  
    
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      