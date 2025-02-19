import turtle

#create a canvas
turtle.Screen().bgcolor("yellow")

sc=turtle.Screen()
sc.setup(800,800)

turtle.title("star window")

#creating turtle object
t=turtle.Turtle()

#1st triangle
t.forward(100)
t.left(120)
t.forward(100)
t.left(120)
t.forward(120)

t.penup()
t.right(150)
t.forward(50)

#2nd triangle
t.pendown()
t.right(90)
t.forward(100)
t.right(120)
t.forward(100)
t.right(120)
t.forward(120)

turtle.done()

