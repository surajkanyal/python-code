from turtle import Turtle,Screen
import random

def draw_shape(n):
    ace= Turtle( shape = 'turtle')
    colors = ['CornflowerBlue','DarkOrchid','IndianRed','DeepSkyBlue','wheat','SlateGray','red', 'green', "blue", "cyan", "lightgreen", "turquoise", 'skyblue']
    myScreen = Screen()
    ace.pensize(7)
    for i in range(n):
        ace.color(random.choice(colors))
        angle = 360/(3+i)
        for j in range(3+i):
            ace.forward(100)
            ace.left(angle)
    myScreen.exitonclick()
n = 9
draw_shape(n)