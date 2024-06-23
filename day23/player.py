import turtle

STARTING_POSITION = (0, -280)
MOVE_DISTANCE = 10
FINISH_LINE_Y = 280


class Player(turtle.Turtle):
    
    def __init__(self):
        super().__init__()
        self.shape("turtle")
        self.penup()
        self.goto(STARTING_POSITION)
        self.left(90)
        turtle.onkey(self.move, "Up")
        turtle.listen()

    def move(self):
        self.forward(10)

    def win(self):
        if self.ycor() >= 280:
            self.goto(STARTING_POSITION)
            return True
        return False

