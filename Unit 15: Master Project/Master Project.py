import turtle
import random


b = turtle.Turtle()
screen = turtle.Screen()
b.penup()
b.goto(-360,-180)
b.pendown()
b.forward(100)
b.right(90)
b.forward(100)
b.left(90)
b.forward(100)
b.left(90)
b.forward(300)
b.right(90)
b.forward(250)
b.right(90)
b.forward(300)
b.left(90)
b.forward(100)
b.left(90)
b.forward(100)
b.right(90)
b.forward(150)


c = turtle.Turtle()
c.penup()
c.goto(0,20)
c.left(90)
c.pendown()
c.color("red")
c.forward(40)
c.right(90)
c.forward(20)
c.left(90)
c.forward(20)
c.left(90)
c.forward(20)
c.left(90)
c.forward(60)
                          

e = turtle.Turtle()
e.penup()
e.goto(-100,20)
e.left(90)
e.pendown()
e.color("blue")
e.forward(40)
e.right(90)
e.forward(20)
e.left(90)
e.forward(20)
e.left(90)
e.forward(20)
e.left(90)
e.forward(60)

s = turtle.Turtle()
s.penup()
s.goto(-300,-180)
s.color("blue")
def right():
  s.right(10)

def left():
  s.left(10)


def up():
  s.forward(10)

def down():
  s.forward(-10)
  
screen.onkey(left,"left")
screen.onkey(right,"right")  
screen.onkey(up,"up")
screen.onkey(down,"down")

a = turtle.Turtle()
a.penup()
a.goto(300,-180)
a.color("red")
def d():
  a.right(10)

def a1():
  a.left(10)

def s1():
  a.forward(-10)

def w():
  a.forward(10)
  
screen.onkey(a1,"a")
screen.onkey(d,"d")  
screen.onkey(w,"w")
screen.onkey(s1,"s")

screen.listen()

blueFlag = 0

redFlag = 0
  
bluestole = 0

redstole = 0
 
bluescore = 0

redscore = 0
 
bs = turtle.Turtle()
bs.penup()
bs.goto(-300,250)
bs.write("bluescore:" + str(bluescore))
   
rs = turtle.Turtle()
rs.penup()
rs.goto(-300,270)
rs.write("redscore:" + str(redscore))
    
 
 
 
 
while True:
  #blue
  e.forward(0)
  if -100 <= s.xcor() <= -80 and 20 <= s.ycor() <= 80 and blueFlag == 0:
    e.clear()
    blueFlag = 1
  if -360 <= s.xcor() <= -260 and -190 <= s.ycor() <= -170 and blueFlag == 1:
    e.penup()
    e.goto(-300,-180)
    e.pendown()
    e.right(180)
    e.color("blue")
    e.forward(40)
    e.right(90)
    e.forward(20)
    e.left(90)
    e.forward(20)
    e.left(90)
    e.forward(20)
    e.left(90)
    e.forward(60)
    blueFlag = 2



  if 0 <= a.xcor() <= 20 and 20 <= a.ycor() <= 80 and redFlag== 0:
    c.clear()
    redFlag = 1
  if 240 <= a.xcor() <= 400 and -190 <= a.ycor() <=  -170 and redFlag == 1:
    c.penup()
    c.goto(270,-180)
    c.pendown()
    c.right(180)
    c.color("red")
    c.forward(40)
    c.right(90)
    c.forward(20)
    c.left(90)
    c.forward(20)
    c.left(90)
    c.forward(20)
    c.left(90)
    c.forward(60)
    redFlag = 2
    
  if -15 <= s.xcor() -a.xcor() <= 15 and -15 <= s.ycor() -a.ycor() <= 15:
    if s.xcor() < 0:
      a.goto(270,-180)
      if redstole == 1:
        redstole = 0
        e.penup()
        e.goto(-300,-180)
        e.pendown()
        e.right(180)
        e.color("blue")
        e.forward(40)
        e.right(90)
        e.forward(20)
        e.left(90)
        e.forward(20)
        e.left(90)
        e.forward(20)
        e.left(90)
        e.forward(60)
    else:
      s.goto(-300,-180)
      if bluestole == 1:
        bluestole = 0
        c.penup()
        c.goto(270,-180)
        c.pendown()
        c.right(180)
        c.color("red")
        c.forward(40)
        c.right(90)
        c.forward(20)
        c.left(90)
        c.forward(20)
        c.left(90)
        c.forward(20)
        c.left(90)
        c.forward(60)
        
      
  if -300 <= a.xcor() <= -280 and -180 <= a.ycor() <= -120 and blueFlag == 2 and redFlag == 2:
    e.clear()
    redstole = 1
      

  if 270 <= s.xcor() <= 290 and -180 <= s.ycor() <= -120 and redFlag == 2 and blueFlag == 2:
    c.clear()
    bluestole = 1

  if s.xcor() <= 0 and bluestole ==1:
    bluestole = 2 
    bluescore = bluescore + 1
    bs.clear()
    bs.write("bluescore:" + str(bluescore))
    
  if a.xcor() >= 0 and redstole ==1:
    redstole = 2 
    redscore = redscore + 1
    rs.clear()
    rs.write("redscore:" + str(redscore))














