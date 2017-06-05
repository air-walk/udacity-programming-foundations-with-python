import turtle

def draw_square(some_turtle):
    for i in range(0, 4):
        some_turtle.forward(100)
        some_turtle.right(90)

def draw_triangle(some_turtle):
    for i in range(0, 3):
        some_turtle.forward(100)
        some_turtle.left(120)    

def draw_art():
    window = turtle.Screen()
    window.bgcolor("red")
    
    brad = turtle.Turtle()
    brad.shape("circle")
    brad.color("black")
    brad.speed(3)

    for i in range(0, 36):
        draw_square(brad)
        brad.right(10)

    window.exitonclick()

draw_art()

