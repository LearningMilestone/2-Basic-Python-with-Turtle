'''Example: X and Y Axes with Hash Marks
Tracy will draw x and y axes on the screen and will place hash marks at every 25 pixels.

*Notice how the function is defined at the top of the code before being used!'''
from turtle import *
tracy=Turtle('turtle')
screen=Screen()
##################################
#Write your code here############
#################################
tracy.speed(5)

# This function will draw a line with hash marks at every 25 pixels.
def draw_hashed_axis():
    tracy.pendown()
    for i in range(16):
        tracy.forward(25)
        tracy.right(90)
        tracy.forward(10)
        tracy.backward(20)
        tracy.forward(10)
        tracy.left(90)

# Move Tracy to top of canvas and call draw hash marks function for y-axis.
# Then move Tracy to left of canvas and call hash marks function for x-axis.
tracy.penup()
tracy.setposition(0,200)
tracy.right(90)
draw_hashed_axis()
tracy.penup()
tracy.setposition(-200,0)
tracy.left(90)

draw_hashed_axis()
##fixed section###################
screen.exitonclick()

