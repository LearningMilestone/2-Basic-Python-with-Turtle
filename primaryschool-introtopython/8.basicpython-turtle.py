'''Example: Asterisk
Tracy will draw an asterisk in the middle of the canvas with lines 100 pixels long.'''
from turtle import *
tracy=Turtle('turtle')
screen=Screen()
##################################
#Write your code here############
#################################

tracy.speed(5)
tracy.left(30)
for i in range(6):
    tracy.forward(100)
    tracy.backward(100)
    tracy.left(60)

##fixed section###################
screen.exitonclick()

