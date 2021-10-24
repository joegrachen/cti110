import turtle
wn = turtle.Screen()
wn.bgcolor("light blue")
turtle.color("white")

turtle.penup()
turtle.forward(90)
turtle.left(45)
turtle.pendown()

def branch():
    for i in range(3):
        for i in range(3):
          turtle.forward(30)
          turtle.backward(30)
          turtle.right(45)
        turtle.left(90)
        turtle.backward(30)
        turtle.left(45)
    turtle.right(90)
    turtle.forward(90)

for i in range(8):
    branch()
    turtle.left(45)

wn.exitonclick
