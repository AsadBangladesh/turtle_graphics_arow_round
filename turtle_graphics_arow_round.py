
import turtle 
aj = turtle.Turtle()
aj.speed(100)

for i in range(180):
    aj.forward(150)
    aj.right(30)
    aj.forward(20)
    aj.left(60)
    aj.forward(50)
    aj.right(30)

    aj.penup()
    aj.setposition(0, 0)
    aj.pendown()

    aj.right(5)

turtle.done()