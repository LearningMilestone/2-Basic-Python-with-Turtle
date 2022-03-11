#Tracy will draw two dashes along the x-axis, each 100 pixels long
# with spaces of 100 pixels between each
from turtle import *
tracy=Turtle('turtle')
screen=Screen()
##################################
#Write your code here############
#################################
tracy.penup()
tracy.backward(200)
tracy.pendown()
tracy.forward(100)
tracy.penup()
tracy.forward(100)
tracy.pendown()
tracy.forward(100)
tracy.penup()
tracy.forward(100)
tracy.pendown()

##fixed section###################
screen.exitonclick()

