import turtle as t
import random

ace = t.Turtle(shape = 'turtle')
ace.pensize(4)
ace.speed('fastest')
t.colormode(255)
my_screen = t.Screen()
def gen_random_col():
    r = random.randint(0,255)
    g = random.randint(0,255)
    b = random.randint(0,255)
    colors = (r,g,b)
    return colors
    
def spirals():
    for _ in range(100):
        ace.color(gen_random_col())
        ace.circle(100)
        ace.setheading(ace.heading() + 10)
    my_screen.exitonclick()
    
spirals()
