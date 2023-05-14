import turtle
ninja = turtle.Turtle()
ninja.speed(100)

for i in range(120):
    ninja.forward(250)
    ninja.right(140)
    ninja.forward(10)
    ninja.left(60)
    ninja.forward(40)
    ninja.right(120)

    ninja.penup()
    ninja.setposition(0, 0)
    ninja.pendown()

    ninja.right(1)
    


    
turtle.done()