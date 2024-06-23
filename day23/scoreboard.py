import turtle

FONT = ("Courier", 24, "normal")


class Scoreboard(turtle.Turtle):
    
    def __init__(self):
        super().__init__()
        self.level = 1
        self.appear()
        
    def update(self):
        self.reset()
        self.level += 1
        self.appear()

    def appear(self):
        self.hideturtle()
        self.penup()

        self.goto(-170, 260)
        self.write(f"LEVEL: {self.level}", font=FONT)

    def die(self):
        game_over = turtle.Turtle()
        game_over.penup()
        game_over.write("GAME OVER", align="center", font=FONT)



