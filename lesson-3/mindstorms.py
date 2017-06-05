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

def draw_A(some_turtle):
    some_turtle.left(60)
    some_turtle.forward(100)
    some_turtle.right(120)
    some_turtle.forward(65)
    some_turtle.right(120)
    some_turtle.forward(65)
    some_turtle.penup()
    some_turtle.right(180)
    some_turtle.forward(65)
    some_turtle.pendown()
    some_turtle.right(60)
    some_turtle.forward(100 - 65)
    some_turtle.left(60)

def draw_W(some_turtle):
    some_turtle.penup()
    some_turtle.left(90)
    some_turtle.forward(80)
    some_turtle.right(150)
    some_turtle.pendown()
    some_turtle.forward(85)
    some_turtle.left(100)
    some_turtle.forward(50)
    some_turtle.right(90)
    some_turtle.forward(50)
    some_turtle.left(100)
    some_turtle.forward(100)
   
def draw_initials():
    window = turtle.Screen()
    window.bgcolor("blue")

    dude = turtle.Turtle()
    dude.color("pink")
    dude.speed(1)

    draw_A(dude)

    dude.penup()
    dude.forward(20)
    dude.pendown()
    
    draw_W(dude)

    window.exitonclick()
    
# draw_art()
draw_initials()
