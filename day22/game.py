
import turtle, ball, paddle, score

class Game:
    
    
    def __init__(self):
        self.screen = turtle.Screen()
        self.screen.bgcolor("black")
        self.screen.setup(width=800, height=600)

        #self.screen.tracer(0)
        
        self.paddle_left = paddle.Paddle("left", self.screen)
        self.paddle_right = paddle.Paddle("right", self.screen)

        self.ball = ball.Ball()

        self.score_left = score.Score("left", self.screen)
        self.score_right = score.Score("right", self.screen)

        

        self.screen.listen()
        self.screen.onkeypress(self.paddle_right.go_up, "Up")
        self.screen.onkeypress(self.paddle_right.go_down, "Down")
        self.screen.onkeypress(self.paddle_left.go_up, "w")
        self.screen.onkeypress(self.paddle_left.go_down, "s")
        self.screen.onkeyrelease(self.paddle_right.stop_move, "Up")
        self.screen.onkeyrelease(self.paddle_right.stop_move, "Down")
        self.screen.onkeyrelease(self.paddle_left.stop_move, "w")
        self.screen.onkeyrelease(self.paddle_left.stop_move, "s")

        

    
    def test(self):
        while True:
            #self.screen.update()
            self.ball.move()

    
    def start(self):
        #self.ball.start()
        self.game_is_on = True
        
        while self.game_is_on:
            #self.screen.update()
            self.ball.move()
            
        
            if self.ball.collide(self.paddle_left, self.screen) or self.ball.collide(self.paddle_right, self.screen):
                self.ball.change_xdir()
            elif self.ball.hit_side(self.screen):
                self.ball.change_ydir()
            elif self.ball.leave_left(self.screen):
                self.score_right.add_point()
            elif self.ball.leave_right(self.screen):
                self.score_left.add_point()
           
        self.screen.exitonclick() 
            
    