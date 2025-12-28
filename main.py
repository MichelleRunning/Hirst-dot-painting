import turtle
import random
import colorgram

# Allow RGB colors (0–255)
turtle.colormode(255)

# Create the turtle
tim = turtle.Turtle()
tim.speed("fastest")
tim.penup()
tim.hideturtle()

# -------------------- GET COLORS FROM IMAGE --------------------

colors = colorgram.extract("image.jpg", 15)
color_list = []

for color in colors:
    r = color.rgb.r
    g = color.rgb.g
    b = color.rgb.b
    color_list.append((r, g, b))

# -------------------- MOVE TO START POSITION --------------------

tim.setheading(225)
tim.forward(300)
tim.setheading(0)

# -------------------- DRAW DOT PAINTING --------------------

number_of_rows = 10
number_of_dots = 10
dot_size = 20
space_between = 50

for row in range(number_of_rows):
    for dot in range(number_of_dots):
        tim.dot(dot_size, random.choice(color_list))
        tim.forward(space_between)

    # Move up to the next row
    tim.setheading(90)
    tim.forward(space_between)
    tim.setheading(180)
    tim.forward(space_between * number_of_dots)
    tim.setheading(0)

# Exit on click
turtle.Screen().exitonclick()
