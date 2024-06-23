import time
import turtle
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)

player = Player()
scores = Scoreboard()
cm = CarManager()

game_is_on = True


while game_is_on:

    time.sleep(0.1)
    screen.update()
    cm.create_next_wave()
    cm.move_cars()

    if cm.collide_player(player):
        game_is_on = False
        scores.die()
    
    if player.win():
        cm.add_level()
        scores.update()
        print("baszás")

screen.exitonclick()

