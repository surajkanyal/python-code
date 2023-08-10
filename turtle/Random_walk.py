import turtle as t 
import random

ace = t.Turtle(shape ='turtle')
myScreen = t.Screen()
t.colormode(255)

ace.pensize(6)
ace.speed('fast')

direction = [0,90,180,270]

def gen_random_colors():
    r = random.randint(0,255)
    g = random.randint(0,255)
    b = random.randint(0,255) 

    colors = (r,g,b)
    return colors
def gen_random_walk():
    for _ in range(100):
        ace.color(gen_random_colors())
        ace.forward(30)
        ace.setheading(random.choice(direction))
    myScreen.exitonclick()

gen_random_walk()