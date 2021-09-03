#!/usr/bin/env python
# coding: utf-8

'''
Turtle starter code
ATLS 1300
Author: Dr. Z
Author: YOUR NAME
May 29, 2020
'''

import turtle #import the library of commands that you'd like to use

turtle.colormode(255)

# Create a panel to draw on. 
panel = turtle.Screen()
w = 750 # width of panel
h = 750 # height of panel
panel.setup(width=w, height=h) #600 x 600 is a decent size to work on. 
#You can experiment by making it the size of your screen or super tiny!

# Create a colorful background and add Bezos image to it
image = "Bezos.gif"
panel.bgcolor("lightsteelblue1")
panel.bgpic(image)

#=======Add your code here======
turtle.penup()
turtle.goto(4, 64)
turtle.color("black")
turtle.pendown()
turtle.pensize(10)
turtle.forward(40)
turtle.penup()

turtle.pensize(2)
turtle.penup()
turtle.goto(-15, 108)
turtle.color("red")
turtle.pendown()
turtle.begin_fill()
turtle.circle(3)
turtle.end_fill()

turtle.penup()
turtle.goto(42, 118)
turtle.pendown()
turtle.begin_fill()
turtle.circle(3)
turtle.end_fill()

turtle.goto(500, -300)
turtle.penup()
turtle.goto(-15, 108)
turtle.pendown()
turtle.goto(500, -300)
turtle.penup()

turtle.goto(-140, 185)
turtle.begin_fill()
turtle.pendown()
turtle.color("black")
turtle.goto(-94, 185)
turtle.goto(-94, 285)
turtle.goto(52, 285)
turtle.goto(52, 185)
turtle.goto(-140, 185)
turtle.end_fill()
turtle.goto(116, 185)

turtle.penup()

turtle.goto(-300, 200)
turtle.color("green")
turtle.pendown()
turtle.begin_fill()
turtle.forward(100)
 
turtle.left(120)
turtle.forward(100)
 
turtle.left(120)
turtle.forward(100)
turtle.end_fill()
turtle.penup()

turtle.goto(-260, 240)
turtle.pendown()
turtle.color("red")
turtle.begin_fill()
turtle.circle(20)
turtle.end_fill()

turtle.hideturtle()


#=======Clean up code (do not change)======
# this code ensures that your script runs correctly each time.
turtle.done()
