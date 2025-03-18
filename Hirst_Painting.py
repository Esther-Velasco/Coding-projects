
"""
TODO 1.
Print a list containing tuples of three integers each, with all colours in the
 image.

import colorgram

#Extract colors from an image
colors = colorgram.extract("image.jpg",30)
first_color = colors[0] # first element of the list with multiple info
rgb_first_color = first_color.rgb # accesing the red of the first color
print(rgb_first_color[0])

def generate_tuple_colors(list_of_colors):
    list_rgb = []
    for color in list_of_colors: 
        red = color.rgb[0]
        green = color.rgb[1]
        blue = color.rgb[2]
        rgb = (red,green,blue)
        list_rgb.append(rgb)
        #return list with tuples having color codes in rgb
    return list_rgb


generate_tuple_colors(colors)
#checking length
#len(colors)

"""


"""
TODO 2.
Use turtle graphics to create a spots-painting.
Requirements:
- frame size = 10 x 10 rows
- spot size = 20 and 50 paces of space between each
- random color for each dot, from the color palette in the image selected above
"""
# TODO 2.1 Importing necessary packages
import turtle as t 
import random


#Pasting the color list extracted from the code above
color_list = [
 (133, 164, 202),
 (225, 150, 101),
 (30, 43, 64),
 (201, 136, 148),
 (163, 59, 49),
 (236, 212, 88),
 (44, 101, 147),
 (136, 181, 161),
 (148, 64, 72),
 (51, 41, 45),
 (161, 32, 29),
 (60, 115, 99),
 (59, 48, 45),
 (170, 29, 32),
 (215, 83, 73),
 (236, 167, 157),
 (230, 163, 168),
 (36, 61, 55),
 (15, 96, 71),
 (33, 60, 106),
 (172, 188, 219),
 (194, 99, 108),
 (106, 126, 158),
 (18, 83, 105),
 (175, 200, 188),
 (35, 150, 209)
 ]

# Making sure the sreen is set for RGB colors
t.colormode(255)

# TODO 2.2 Create the turtle and give it the round shape with a size of 10
dotty = t.Turtle()
dotty.speed(5)
increment = 50

# Center the drawing in the screen so we see whats happening

# TODO 2.3  Make the turtle paint a dot every 50 paces

#Set heading so that the drawing fits on screen

 
#dotty.setheading(225)
#dotty.penup()
#dotty.forward(300)
#dotty.setheading(0)
# to know where I should start
#print(dotty.pos()) = (-212.13,-212.13)
starting_y = -212.13
dotty.teleport(-212.13,starting_y)

for rows in range(10):
    for columns in range(10):
        dotty.color(random.choice(color_list))
        dotty.dot(10)
        dotty.penup()
        dotty.forward(50)
    starting_y += increment
    new_position = dotty.teleport(x = -212.13, y = starting_y)

# TODO 2.5 Make colors random
# TODO 2.6 Show the screen and exit on click
frame_screen = t.Screen()
frame_screen.screensize(1000,1000)	
frame_screen.exitonclick()




