import turtle
t = turtle.Turtle()
b = turtle.Turtle()
s = turtle.Turtle()
screen = turtle.Screen() 
t.goto (100,5)
s.penup()
s.goto(-200,200)

def right():
  t.right(5)

def left():
  t.left(5)

screen.onkey(left,"left")
screen.onkey(right,"right")  


screen.listen()



def right2():
  b.right(5)

def left2():
  b.left(5)

screen.onkey(left2,"a")
screen.onkey(right2,"d")  


screen.listen()

score=0

s.write("score:" + str(score))


while True :
  t.forward (1)
  b.forward(1)
  if -15 <= t.xcor() -b.xcor() <= 15 and -15 <= t.ycor() -b.ycor() <= 15:
    t.write("collided")
    
    score = score + 1
    s.clear()
    s.write("score:" + str(score))
    
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  