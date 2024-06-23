import turtle


class Car(turtle.Turtle):

    def __init__(self, color="red", x=300, y=0) :
        super().__init__("square")
        self.turtlesize(1,2)
        self.penup()
        self.color(color)
        self.goto(x, y)
        self.left(180)

    def move(self, pace=10):
        self.forward(pace)

        
      