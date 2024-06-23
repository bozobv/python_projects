
from tkinter.constants import W
import turtle

class Paddle(turtle.Turtle):
    
    def __init__(self, place, screen):
        super().__init__()
        self.shape("square")
        self.penup()
        self.color("white")
        self.moving = False
        
        if place == "left":
            self.teleport(-screen.window_width()/2+15, 0)
        elif place == "right":
            self.teleport(screen.window_width()/2-20, 0)
        else:
            self.write("vanbaj", True, align="center")

        self.shapesize(8, 1)
        
    def stop_move(self):
        self.moving = False

        
    def go_up(self):
        self.moving = True
        while self.moving:
            self.goto(self.xcor(), self.ycor() + 10)
    
    def go_down(self):
        self.moving = True
        while self.moving:
            self.goto(self.xcor(), self.ycor() - 10)

        
    