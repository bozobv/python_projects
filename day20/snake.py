from hashlib import new
from turtle import Turtle, Screen, TurtleScreen, screensize
import turtle
import time
import random

COLORS = ["red", "orange", "yellow", "green", "blue", "indigo", "violet", "white", "pink", "brown", "gold", "silver", "gray", "purple"]
STARTER_SNAKE_SIZE = 3


class Snake:
    
    def __init__(self, pieces=STARTER_SNAKE_SIZE, x=0, y=0):
        
        x_starter = x
        y_starter = y
        self.body = []
        for i in range(pieces):
            snake_piece = Turtle()
            snake_piece.shape("square")
            snake_piece.color(random.choice(COLORS))
            snake_piece.penup()
            snake_piece.goto(x=(x_starter-i*21), y=y_starter)
            self.body.append(snake_piece)
        
        self.head = self.body[0]
        self.heading = "east"
    
        
    def move_forwards(self):
        for i in range(len(self.body)-1, 0, -1):
            self.body[i].goto(x=self.body[i-1].xcor(), y=self.body[i-1].ycor())
        
        self.body[0].forward(20)
        
        
    def turn_left(self):
        if self.heading != "east":
            self.head.setheading(180)
            self.heading = "west"
    
    def turn_right(self):
        if self.heading != "west":
            self.head.setheading(0)
            self.heading = "east"
        
    def turn_up(self):
        if self.heading != "south":
            self.head.setheading(90)
            self.heading = "north"
    
    def turn_down(self):
        if self.heading != "north":
            self.head.setheading(270)
            self.heading = "south"

    def eat(self, food):
        new_piece = Turtle()
        new_piece.shape("square")
        new_piece.color(food.get_color())
        new_piece.penup()            
        self.body.append(new_piece)
        
    def hit_the_wall(self):
        if self.head.xcor() > 280 or self.head.xcor() < -280 or self.head.ycor() > 280 or self.head.ycor() < -280:
            return True
        return False
    
    def hit_the_tail(self):
        
        for piece in self.body[1:]:
            if self.head.distance(piece) < 10:
                return True
        return False
