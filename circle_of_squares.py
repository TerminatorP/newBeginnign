import turtle

sam = turtle.Turtle()
sam.speed(100)

def square(length,angle):
    sam.forward(length)
    sam.left(angle)
    sam.forward(length)
    sam.left(angle)
    sam.forward(length)
    sam.left(angle)
    sam.forward(length)
for i in range(1000):
    square(100,90)

    sam.left(11)

turtle.done()
