import turtle
import random
t = turtle.Turtle()
t.speed(2)
t.shape("turtle")
t.left(90)
age = random.randint(1,80)
if age < 20:
  t.write("I'm an kid turtle!")
elif age < 60:
  t.write("I'm an adult turtle!")
else:
  t.write("I'm an grampa turtle!")