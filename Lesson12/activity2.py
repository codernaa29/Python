import turtle

turtle.bgcolor("orange")
for i in range(3):
    turtle.forward(100)
    turtle.left(120)
turtle.penup()
turtle.left(90)
turtle.forward(60)
turtle.right(90)
turtle.pendown()
for i in range(3):
    turtle.forward(100)
    turtle.right(120)
turtle.done()