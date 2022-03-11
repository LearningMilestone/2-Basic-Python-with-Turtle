'''Example: Square Using Loops
Tracy will draw a square with sides of length 50 using a for loop.'''
from turtle import *
tracy=Turtle('turtle')
screen=Screen()
##################################
#Write your code here############
#################################
for i in range(4):
    tracy.forward(50)
    tracy.left(90)

##fixed section###################
screen.exitonclick()

