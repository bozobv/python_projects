import turtle

class Score(turtle.Turtle):
    
    def __init__(self, place, screen):
        super().__init__()
        
        self.hideturtle()
        self.penup()
        self.color("white")
        
        
        if place == "left":
            self.teleport(-screen.window_width()/4, screen.window_height()/2-30)
        elif place == "right":
            self.teleport(screen.window_width()/4, screen.window_height()/2-30)
        else:
            self.write("vanbaj", True, align="center")
            
        
        self.write(place, True, align="center", font=("Arial", 16, "bold"))
        
    def add_point(self):
        self.clear()

        
