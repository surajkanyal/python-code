# It is a  turtle graphic library
# You can learn more from turtle library
from turtle import Turtle, Screen  # these are classes of turtle
ace = Turtle()
print(ace)
# change the shaape
ace.shape('turtle')
# lets change the color
ace.color('coral')
#move our turtle by 100 paces
ace.forward(100) 

my_screen = Screen()
print(my_screen.canvheight)
my_screen.exitonclick()  #this helps to retain on screen till the click happens

