from svg_turtle import SvgTurtle

# Turtle without screen
t = SvgTurtle()

t.showturtle()
t.forward(100)
t.left(90)
t.forward(100)
t.left(90)
t.forward(100)


# export to SVG
t.save_as("temp2.svg")