from turtle import *

# Turtle without screen
t = Turtle()
t.forward(100)
t.left(90)
t.forward(100)

# export to SVG
svg = t.getscreen().getcanvas().postscript(file="temp.svg")


