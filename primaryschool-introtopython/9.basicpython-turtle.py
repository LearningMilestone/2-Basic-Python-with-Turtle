'''Example: Four Circles
Tracy will draw four circles in a square formation in the center of the canvas.'''
from turtle import *
tracy=Turtle('turtle')
screen=Screen()
##################################
#Write your code here############
#################################
tracy.speed(5)

tracy.penup()
tracy.setposition(-50,-100)
tracy.fd(10)

for i in range (2):
    tracy.pendown()
    tracy.circle(50)
    tracy.penup()
    tracy.forward(100)

tracy.setposition(-50,0)

for i in range (2):
    tracy.pendown()
    tracy.circle(50)
    tracy.penup()
    tracy.forward(100)

##fixed section###################
screen.exitonclick()

