import turtle

#create a canvas
turtle.Screen().bgcolor("yellow")

sc=turtle.Screen()
sc.setup(500,500)

turtle.title("square window")

#creating turtle object
tut=turtle.Turtle()

#creating a square
for i in range(4):
    tut.forward(200)
    tut.right(90)
    i=i+1
turtle.done()