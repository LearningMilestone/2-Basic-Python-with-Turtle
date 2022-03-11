'''Exercise : Circle Pyramid
Have Tracy create a pyramid of circles with 3 circles on the bottom row,
 2 on the middle row, and 1 on the top.
Your pyramid should:
-rest on the bottom of the canvas
-be centered in the x direction
-have circles of radius 50
-use for loops
Hints:
It would be very helpful to plan out the placement of your pyramid on graph paper and label your coordinates before starting your code!
You can write one for loop to draw the row of 3 circles and reuse it to draw the row of 2 circles- just change the for loop value!
[Extra Challenge: Our circle pyramid has some space between each row
(ie: The circle rows are not all touching). Determine a way to make your pyramid rows all touch.]'''

from turtle import *
tracy=Turtle('turtle')
screen=Screen()
screen.setup(500, 500)
tracy.speed(10)
##################################
#Write your code here############
#################################
tracy.penup()
tracy.setposition(-100,-200)
tracy.pendown()
for i in range(3):
    tracy.circle(50)
    tracy.penup()
    tracy.fd(100)
    tracy.pendown()
tracy.penup()
# tracy.setposition(-50,-100)
tracy.setposition(-50,-115)
tracy.pendown()
for i in range(2):
    tracy.circle(50)
    tracy.penup()
    tracy.fd(100)
    tracy.pendown()
tracy.penup()
#tracy.setposition(0,0)
tracy.setposition(0,-30)
tracy.pendown()
tracy.circle(50)



##fixed section###################
screen.exitonclick()

