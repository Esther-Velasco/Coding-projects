
from turtle import Turtle, Screen
import random

is_race_on = False
screen = Screen()
screen.setup(height = 400, width = 500)
user_bet = screen.textinput(title = "Make your bet", prompt= "Which turtle will win the race? Select a color:") 
colors = ["red", "orange", "yellow","green", "blue","purple"]
all_turtles = []

#I create a dictionary with the starting coordinates
#dict_coordinates = dict(x=-240, y=-100)
dict_coordinates = {
    "x":-230,
    "y":-100
    }

# create 6 turtles - one per color in colors list
# Take turtle to starting line in a vertical and evenly distribution

for color in colors:
    turtle = Turtle(shape="turtle")
    turtle.color(color)
    turtle.penup()
    dict_coordinates['y'] += 30
    turtle.goto(**dict_coordinates)
    all_turtles.append(turtle)

#initialize the game
if user_bet:
    is_race_on = True
    
while is_race_on:
    for turtle in all_turtles:
        if turtle.xcor() > 230: # turtle won / a turtle is 40 pixels wide 
            is_race_on = False
            winning_color = turtle.pencolor()
            if winning_color == user_bet:
                print(f"You won! The {winning_color} turtle is the winner!")
            else:
                print(f"You lost! :( The {winning_color} turtle is the winner.")
    
        rand_distance = random.randint(0,10)
        turtle.forward(rand_distance)
        
screen.exitonclick()

