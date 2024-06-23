from food import Food
from turtle import Turtle, Screen, TurtleScreen, screensize
import turtle
import time
import random
from scoreboard import ScoreBoard
import snake

test_turtle = Turtle()
screen = Screen()


     
        
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("Kelgyós játék")
#animations off
screen.tracer(0)

#test_turtle.shape("square")
#test_turtle.color("white")
#test_turtle.penup()
#test_turtle.speed("normal")

da_snake = snake.Snake()
da_food = Food()
da_score = ScoreBoard()

screen.listen()
turtle.onkeypress(key="Left", fun=da_snake.turn_left)
turtle.onkeypress(key="Right", fun=da_snake.turn_right)
turtle.onkeypress(key="Up", fun=da_snake.turn_up)
turtle.onkeypress(key="Down", fun=da_snake.turn_down)
    
game_ongoing = True

while game_ongoing:
    time.sleep(0.1)
    da_snake.move_forwards()
    screen.update()

    if da_snake.head.distance(da_food) < 15:
        da_snake.eat(da_food)
        da_food.eaten()
        da_score.add_point()
    
    if da_snake.hit_the_wall() or da_snake.hit_the_tail():
        game_ongoing = False
        da_score.game_over()
        
    
screen.exitonclick()
    


