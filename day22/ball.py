import turtle

PACE = 10

class Ball(turtle.Turtle):
    
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.penup()
        self.color("white")
        self.y_dir = 1
        self.x_dir = 1
    
    def move(self):
        new_x = self.xcor() + self.x_dir * PACE
        new_y = self.ycor() + self.y_dir * PACE
        self.goto(new_x, new_y)
        
    def change_xdir(self):
        self.x_dir *= -1
        
    def change_ydir(self):
        self.y_dir *= -1
        
    def reset_position(self):
        self.teleport(0, 0)
        self.change_ydir()
        self.change_xdir()
        
    def collide(self, de_paddle, screen):
        if self.distance(de_paddle) < 90 and (self.xcor() > screen.window_width()/2 - 40 or self.xcor() < -screen.window_width()/2 + 40) : 
            return True
        return False
        
    
    def hit_side(self, screen):
        if self.ycor() > screen.window_height()/2 - 10 or self.ycor() < -screen.window_height()/2 + 10 :
            print("ÁÁÁÁÁÁÁÁÁÁÁÁÁÁÁÁÁ")
            return True
        return False
                
    def leave_left(self, screen):
        if self.xcor() > screen.window_width()/2 - 10:
            self.reset_position()
            return True
        return False
    
    def leave_right(self, screen):
        if self.xcor() < -screen.window_width()/2 + 10:
            self.reset_position()
            return True
        return False
