import turtle

turtle = turtle.Turtle()
turtle.speed(20)

def square(length,angle):
    turtle.forward(length)
    turtle.left(angle)
    turtle.forward(length)
    turtle.left(angle)
    turtle.forward(length)
    turtle.left(angle)
    turtle.forward(length)
for i in range(10000):
    square(10,11)
    

