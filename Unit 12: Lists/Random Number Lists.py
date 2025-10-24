import turtle
import random
t = turtle.Turtle()
numbers = []
t.penup()
t.goto(-150,0)
t.left(0)
t.pendown()
for i in range(15):
  numbers.append(random.randint(1,30))
for number in numbers:
  t.write(number)
  t.forward(30)
t.penup()
t.goto(-150,-30)
t.left(0)
t.pendown()
for number in numbers:
  t.write(number + 10)
  t.forward(30)
t.penup()
t.goto(-150,-60)
t.left(0)
t.pendown()
for number in numbers:
  t.write(number + 100)
  t.forward(30)
t.penup()
t.goto(-150,-90)
t.left(0)
t.pendown()
for number in numbers:
  t.write(number + 1000)
  t.forward(30)
t.penup()
t.goto(-150,-120)
t.left(0)
t.pendown()
for number in numbers:
  t.write(number + 10000)
  t.forward(30)
t.penup()
t.goto(-150,-150)
t.left(0)
t.pendown()
for number in numbers:
  t.write(number + 100000)
  t.forward(30)
t.penup()
t.goto(-150,-180)
t.left(0)
t.pendown()
for number in numbers:
  t.write(number + 100000)
  t.forward(30)
  
  
  
  
  
  
  
  
  
  
  
  