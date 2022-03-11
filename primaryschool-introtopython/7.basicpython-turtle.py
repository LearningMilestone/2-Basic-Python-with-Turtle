'''Example: Dotted Line
Tracy will draw a dotted line across the canvas'''
from turtle import *
tracy=Turtle('turtle')
screen=Screen()
##################################
#Write your code here############
#################################
tracy.penup()
tracy.backward(200)

for i in range (40):
    tracy.pendown()
    tracy.forward(5)
    tracy.penup()
    tracy.forward(5)

##fixed section###################
screen.exitonclick()

