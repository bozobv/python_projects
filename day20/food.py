import turtle
import random

COLORS = ["red", "orange", "yellow", "green", "blue", "indigo", "violet", "white", "pink", "brown", "gold", "silver", "gray", "purple"]

class Food(turtle.Turtle):
    
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.penup()
        self.shapesize(stretch_len=0.5, stretch_wid=0.5)
        self.color(random.choice(COLORS))
        self.speed("fastest")

        self.placing()
        
        
    def placing(self):
        random_x = random.randint(-280, 280)
        random_y = random.randint(-280, 280)
        self.goto(random_x, random_y)
        
    def get_color(self):
        print(self.color()[0])
        return self.color()[0]
           
    def eaten(self):
        self.color(random.choice(COLORS))
        random_x = random.randint(-280, 280)
        random_y = random.randint(-280, 280)
        self.goto(random_x, random_y)
