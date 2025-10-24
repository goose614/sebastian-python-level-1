import turtle
t = turtle.Turtle()
colors = []
colors.append("red")
colors.append("turquoise")
colors.append("dark green")
colors.append("light blue")
colors.append("yellow")
for color in colors:
  #do something with color
  t.color(color)
  t.forward(10)
if "purple" in colors:
  t.write("yes")
else :
  t.write("no")