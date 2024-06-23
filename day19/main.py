from turtle import Shape, Turtle, Screen, clear, color, fillcolor, pencolor
import turtle
import random

screen = Screen()
colors = ["red", "orange", "yellow", "green", "blue", "indigo", "violet", "black", "white", "pink", "brown", "gold", "silver", "gray", "purple"]


def move_forwards():
    tim.forward(10)

def turn_left():
    tim.left(5)
    
def turn_right():
    tim.right(5)
    
def move_bacwards():
    tim.back(10)

def reseting():
    tim.home()
    tim.clear()

def create_turtles(num):
    turtle_dict = {}
    for i in range(num):
        turtle_dict[colors[i]] = Turtle(shape="turtle")
        turtle_dict[colors[i]].penup()
        turtle_dict[colors[i]].fillcolor(colors[i])
        
    return turtle_dict

def turtle_to_start(turtles, screen=screen):
    x = -screen.window_width()/2 + 20
    
    height_gap_size = screen.window_height() / (len(turtles) + 1)
    
    y = -screen.window_height() / 2
    
    for little_turtle in turtles:
        y += height_gap_size
        turtles[little_turtle].goto(x=x, y=y)


    
#screen.listen()
#turtle.onkeypress(key="Up", fun=move_forwards)
#turtle.onkeypress(key="Left", fun=turn_left)
#turtle.onkeypress(key="Right", fun=turn_right)
#turtle.onkeypress(key="Down", fun=move_bacwards)
#turtle.onkeypress(key="c", fun=reseting)

screen.setup(width=500, height=400)

#tim = Turtle(shape="turtle")
#tim.fillcolor("red")

user_bet = screen.textinput(title="tedd meg a téted", prompt="Melyik teknőc fog elősz9r célba érni? írd ide a színét: ")
turtle_num = 3
turtles = create_turtles(turtle_num)
turtle_to_start(turtles=turtles)

is_race_on = False

if user_bet:
    is_race_on = True

while is_race_on:
    
    for turtle in turtles:
        rand_dist = random.randint(0, 10)
        turtles[turtle].forward(rand_dist)
        
        if turtles[turtle].xcor() > 230:
            is_race_on = False
            winning_color = turtle
            if winning_color == user_bet:
                print(f"Eltaláltad, a győztes teknőc a {winning_color}!!!!!!")
            else:
                print(f"Nem találtad el, a győztes teknőc a {winning_color}!!!!!!")

            



screen.exitonclick()

