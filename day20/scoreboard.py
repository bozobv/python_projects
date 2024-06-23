import turtle


class ScoreBoard(turtle.Turtle):
    
    def __init__(self) :
        super().__init__()
        self.color("white")
        self.penup()
        self.goto(0, 250)
        self.score = 0
        self.pendown()
        self.write(f"Az eddig megevett finomságok számna:  {self.score}", align="center", font=("Arial", 18, "bold"))
        self.hideturtle()
        
    def add_point(self):
        self.score += 1  
        self.clear()   
        self.write(f"Az eddig megevett finomságok számna:  {self.score}", align="center", font=("Arial", 18, "bold"))
        
    def game_over(self):
        self.goto(0,0)
        self.write("Vége van pöcskös!", align="center", font=("Arial", 18, "bold"))
   
