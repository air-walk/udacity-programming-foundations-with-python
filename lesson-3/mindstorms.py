import turtle

def draw_square():
    brad = turtle.Turtle()
    brad.shape("circle")
    brad.color("black")
    brad.speed(3)

    i     = 0
    times = 4

    while(i < times):
        brad.forward(100)
        brad.right(90)
        i = i + 1

def draw_circle():
    angie = turtle.Turtle()
    angie.shape("arrow")
    angie.color("blue")
    angie.circle(100)

window = turtle.Screen()
window.bgcolor("red")

draw_square()
draw_circle()

window.exitonclick()
